import logging


# Default level is WARNING
# logging.warning('haha')
# logging.info('keke')

# Must be set before using logging, or won't work.
logging.basicConfig(filename='sample.log', level=logging.DEBUG)

logging.debug('what')
logging.info('why')
logging.warn('how')

var = 'apple'
# old style
logging.info('%s', var)
# new style
logging.info('{}'.format(var))
