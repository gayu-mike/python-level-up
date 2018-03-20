import logging


fmt = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'
datefmt = '%m/%d/%Y %I:%M:%S %p'

logging.basicConfig(format=fmt, level=logging.INFO, datefmt=datefmt)

logging.debug('not on console')
logging.info('on console')
logging.warning('on console')
