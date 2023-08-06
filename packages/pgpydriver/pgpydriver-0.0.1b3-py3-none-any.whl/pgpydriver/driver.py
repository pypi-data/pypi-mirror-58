import asyncio
import os
import re
import logging
import sys
from functools import partial
from typing import (
    Iterator, Optional, Tuple, Union, Awaitable, TypeVar
)

import psycopg2 as psql
import psycopg2.extensions as psqlex
from psycopg2 import connect
from psycopg2.pool import SimpleConnectionPool
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.extras import DictCursor, execute_values
from tornado.concurrent import Future, chain_future, future_set_exc_info
from tornado.ioloop import IOLoop
from multiprocessing import cpu_count
from concurrent.futures.thread import ThreadPoolExecutor

from ._querydata import _QeryData
from .querydata import QueryData
from .querytype import QueryType

_T = TypeVar('_T')

logger = logging.getLogger(__name__)


class PostgreDriver:

    POSTGRES_HOST = "POSTGRES_HOST"
    POSTGRES_DB = "POSTGRES_DB"
    POSTGRES_USER = "POSTGRES_USER"
    POSTGRES_PASSWORD = "POSTGRES_PASSWORD"
    POSTGRES_PORT = "POSTGRES_PORT"
    THREAD_CPU_COUNT = "THREAD_CPU_COUNT"

    def get_loop(self):
        return IOLoop.current()

    def __init__(self, **kwargs: dict):
        """
        Parameters
        ----------------------------------------------------------------
        HOST        ホスト名
        DB          データベース名
        USER        ユーザー名
        PASSWORD    パスワード
        PORT        接続ポート

        環境変数:POSTGRES_HOST
        環境変数:POSTGRES_DB
        環境変数:POSTGRES_USER
        環境変数:POSTGRES_PASSWORD
        環境変数:POSTGRES_PORT
        ----------------------------------------------------------------
        """
        self.cpu_count = cpu_count() * int(os.environ.get(self.THREAD_CPU_COUNT, 10))
        self._executer = ThreadPoolExecutor(max_workers=self.cpu_count)
        self.Connection = None
        self.host = os.environ.get(self.POSTGRES_HOST, kwargs.get("HOST"))
        self.dbname = os.environ.get(self.POSTGRES_DB, kwargs.get("DB"))
        self.user = os.environ.get(self.POSTGRES_USER, kwargs.get("USER"))
        self.password = os.environ.get(
            self.POSTGRES_PASSWORD, kwargs.get("PASSWORD"))
        port = os.environ.get(self.POSTGRES_PORT, kwargs.get('PORT', '5432'))
        self.port = int(port)
        self.loop: "IOLoop" = kwargs.get('loop', self.get_loop())
        self.fileno = None

    def connect_async(self) -> "Future[_T]":
        return_future = Future()

        def _connection(fut: "Future[_T]"):
            if not self.is_future_exception(fut, return_future):
                return
            self.Connection = fut.result()
            return_future.set_result(self.Connection)

        future_con = self._executer.submit(partial(connect,
                                                   host=self.host,
                                                   database=self.dbname,
                                                   user=self.user,
                                                   password=self.password,
                                                   port=self.port))
        self.loop.add_future(future_con, _connection)
        return return_future

    def connect(self):
        if not self.Connection:
            self.Connection = connect(
                host=self.host, database=self.dbname, user=self.user, password=self.password, port=self.port)

    def _query(self, kwargs: dict) -> Union[_QeryData, QueryData, int, None]:
        sql = kwargs.pop('sql')
        data = kwargs.pop('data')

        def query_type():
            _sql = sql[:6]
            if re.search(r"select", _sql, re.IGNORECASE):
                return QueryType.select
            elif re.search(r'update', _sql, re.IGNORECASE):
                return QueryType.update
            elif re.search(r'delete', _sql, re.IGNORECASE):
                return QueryType.delete
            elif re.search(r'insert', _sql, re.IGNORECASE):
                return QueryType.insert
            else:
                return QueryType.etc

        self.type = query_type()
        if self.Connection:
            cur = self.Connection.cursor(cursor_factory=DictCursor)
            cur.execute(sql, data)
            return cur
        return None

    def execute_async(self, sql: str, data: Union[tuple, list, None] = None, **kwargs: dict) -> "Future[_T]":
        """
        Return
        --------------------------------------------------------

        * １件取得時  ： _QueryData or None

        * 複数件取得  ： QueryData

        * 登・更・削  ： int, Connection Object
        """
        return_future = Future()
        future_con: "Future[_T]" = None
        if not isinstance(sql, str):
            sql = str(sql)
        kwargs['sql'] = sql
        kwargs['data'] = data
        if not self.Connection:
            future_con = self.connect_async()

        def _execute(fut: "Future[_T]"):
            if not self.is_future_exception(fut, return_future):
                return
            cursor = fut.result()

            def _fetch_all_result(_fut: "Future[_T]"):
                if not self.is_future_exception(_fut, return_future):
                    return
                cur_data = _fut.result()
                if cur_data:
                    return_future.set_result(
                        QueryData(cur_data, cursor.rowcount))
                    cursor.close()
                else:
                    return_future.set_result(QueryData([], 0))
                    cursor.close()

            def _fetch_one_result(_fut: "Future[_T]"):
                if not self.is_future_exception(_fut, return_future):
                    return
                cur_data = _fut.result()
                if cur_data:
                    return_future.set_result(_QeryData(cur_data))
                    cursor.close()
                else:
                    return_future.set_result(_QeryData({}))
                    cursor.close()

            if cursor:
                # 正しくConnectionが張られている時
                if self.type == QueryType.select:
                    if kwargs.get('cnt', 0) == 1:
                        future_cur = self._executer.submit(cursor.fetchone)
                        self.loop.add_future(future_cur, _fetch_one_result)
                    else:
                        future_cur = self._executer.submit(cursor.fetchall)
                        self.loop.add_future(future_cur, _fetch_all_result)
                else:
                    return_future.set_result(cursor.rowcount)
                    cursor.close()
            else:
                if self.type == QueryType.select:
                    if kwargs.get('cnt', 0) == 1:
                        return_future.set_result(_QeryData({}))
                    else:
                        return_future.set_result(QueryData([], 0))
                else:
                    return_future.set_result(0)

        def add_future(fut: "Future[_T]"):
            future_th = self._executer.submit(self._query, kwargs)
            self.loop.add_future(future_th, _execute)

        if future_con:
            self.loop.add_future(future_con, add_future)
        else:
            future_th = self._executer.submit(self._query, kwargs)
            self.loop.add_future(future_th, _execute)
        return return_future

    def is_future_exception(self, future: 'Future[_T]', return_future: 'Future[_T]'):
        exc = future.exception()
        if exc:
            logger.exception(exc, exc_info=sys.exc_info())
            return_future.set_exception(exc)
            return False
        return True

    def execute(self, sql: str, data: Union[tuple, list, None] = None, **kwargs: dict) -> Awaitable[_T]:
        """
        Return
        --------------------------------------------------------

        * １件取得時  ： _QueryData or None

        * 複数件取得  ： QueryData

        * 登・更・削  ： int, Connection Object
        """
        if not isinstance(sql, str):
            sql = str(sql)
        kwargs['sql'] = sql
        kwargs['data'] = data
        cur = self._query(kwargs)
        if self.type == QueryType.select:
            if kwargs.get('cnt', 0) == 1:
                data = cur.fetchone()
                cur.close()
                return _QeryData(data)
            else:
                data = cur.fetchall()
                rowcount = cur.rowcount
                cur.close()
                return QueryData(data, rowcount)
        else:
            rowcount = cur.rowcount
            cur.close()
            return rowcount

    def _copy_from(self, kwargs):
        try:
            f = kwargs['f']
            tableName = kwargs['tableName']
            sep = kwargs['sep']
            null = kwargs['null']
            columns = kwargs['columns']
            cur = self.Connection.cursor()
            cur.copy_from(f, tableName, sep=sep, null=null, columns=columns)
            return True, None
        except psql.Error as e:
            return False, e.pgerror

    def _get_ioString(self, body: Iterator[Iterator[str]]):
        import io
        data = '\n'.join(['\t'.join(d) for d in body])
        return io.StringIO('\n'.join(data), newline="\n")

    def copy_from_async(self, body, tableName, sep="\t", null='\\N', columns=None):
        f = self._get_ioString(body)
        kwargs = {
            'f': f,
            'tableName': tableName,
            'sep': sep,
            'null': null,
            'columns': columns
        }
        future = self.loop.run_in_executor(
            self._executer, self._copy_from, kwargs)
        return future

    def copy_from(self, body, tableName, sep="\t", null='\\N', columns=None):
        f = self._get_ioString(body)
        kwargs = {
            'f': f,
            'tableName': tableName,
            'sep': sep,
            'null': null,
            'columns': columns
        }
        data, e = self._copy_from(kwargs)
        if data:
            return data
        else:
            raise Exception(e)

    def bulk_insert(self, tableName, datas: Iterator[Iterator[object]]):
        cur = self.Connection.cursor()
        sql = 'insert into {tableName} values %s'.format(tableName=tableName)
        return execute_values(cur, sql, datas)

    def _bulk_insert(self, kwargs):
        cur = self.Connection.cursor()
        sql = kwargs['sql']
        datas = kwargs['datas']
        return execute_values(cur, sql, datas)

    def bulk_insert_async(self, tableName, datas: Iterator[Iterator[object]]):
        try:
            sql = 'insert into {tableName} values %s'.format(
                tableName=tableName)
            k = {
                'sql': sql,
                'datas': datas
            }
            future = self.loop.run_in_executor(
                self._executer, self._bulk_insert, k)
            return future
        except Exception as e:
            raise e

    @staticmethod
    def query(sql: str, data: Union[tuple, list, None] = None, **kwargs: dict) -> Union[_QeryData, QueryData, Tuple[_T, 'PostgreDriver'], None]:
        posgre: 'PostgreDriver' = PostgreDriver()
        posgre.connect()
        data = posgre.execute(sql, data, **kwargs)
        if posgre.type != QueryType.select:
            return data, posgre
        else:
            if kwargs.get('returnConnection', False):
                return data, posgre
        del posgre
        return data

    @staticmethod
    async def query_async(sql: str, data: Union[tuple, list, None] = None, **kwargs: dict) -> Union[_QeryData, QueryData, Tuple[_T, 'PostgreDriver'], None]:
        """
        Return
        --------------------------------------------------------
            １件取得時  ： _QueryData or None
            複数件取得  ： QueryData
            登・更・削  ： int,Connection Object
        """
        posgre: 'PostgreDriver' = PostgreDriver()
        data = await posgre.execute_async(sql, data, **kwargs)
        if posgre.type != QueryType.select:
            return data, posgre
        else:
            if kwargs.get('return_connection', False):
                return data, posgre
        del posgre
        return data

    def commit(self):
        self.Connection.commit()

    def rollback(self):
        self.Connection.rollback()

    def close(self):
        try:
            self.Connection.close()
        except:
            pass
        try:
            if self._executer:
                self._executer.shutdown(False)
        except:
            pass

    def send_notifiy(self, _id: str, data: str):
        cur = self.Connection.cursor()
        cur.execute(f'notify "{_id}", %s;', (data,))
        cur.close()

    def listen(self, _id: str):
        cur = self.Connection.cursor()
        cur.execute(f'LISTEN "{_id}";')
        cur.close()

    def poll(self):
        self.Connection.poll()

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_value, trace):
        self.close()

    def __del__(self):
        self.close()

    async def begin_async(self):
        await self.execute_async('begin')

    def begin(self):
        self.execute('begin')

    async def prepared_transaction_async(self):
        from uuid import uuid4
        _id = str(uuid4()).replace('-', '')
        await self.execute_async('prepare transaction %s', (_id,))
        return _id

    def prepared_transaction(self):
        from uuid import uuid4
        _id = str(uuid4()).replace('-', '')
        self.execute('prepare transaction %s', (_id,))
        return _id

    async def commit_prepared_async(self, _id):
        return await self.execute_async('commit prepared %s', (_id,))

    def commit_prepared(self, _id):
        return self.execute('commit prepared %s', (_id,))

    async def rollback_prepared_async(self, _id):
        return await self.execute_async('rollback prepared %s', (_id,))

    def rollback_prepared(self, _id):
        return self.execute('rollback prepared %s', (_id,))
