import logging
from logging.config import fileConfig


fileConfig('logging_config.ini',
           disable_existing_loggers=False)


def log():
    logger = logging.getLogger('ini_bar')
    logging.debug('root')
    logger.debug('ini_bar')
