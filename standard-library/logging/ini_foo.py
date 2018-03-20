import logging
from logging.config import fileConfig

import ini_bar


# disable... defaults to True
fileConfig('logging_config.ini',
           disable_existing_loggers=False)

logger = logging.getLogger('INI')

logger.debug('debug')
ini_bar.log()
logger.critical('critical')
