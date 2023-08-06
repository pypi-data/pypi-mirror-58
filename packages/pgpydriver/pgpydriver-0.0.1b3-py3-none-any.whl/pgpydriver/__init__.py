__version__ = '0.0.1.b3'

import logging
import os
LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO')
parent_logger = logging.getLogger('pgpydriver')
parent_logger.setLevel(logging._nameToLevel[LOGLEVEL])
