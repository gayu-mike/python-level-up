import logging
from logging.config import dictConfig


logging_config = dict(
    version = 1,
    formatters = {
        'f': {
            'format': '%(name)s - %(levelname)s - %(message)s',
        },
    },
    handlers = {
        'h': {
            'class': 'logging.StreamHandler',
            'formatter': 'f',
            'level': logging.DEBUG,
        },
    },
    root = {
        'handlers': ['h'],
        'level': logging.DEBUG,
    }
)

dictConfig(logging_config)

logger = logging.getLogger()
logger.debug('haha')