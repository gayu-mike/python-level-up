import logging
import sys
import time
from logging.handlers import RotatingFileHandler

import dae


def setup_logging():
    logger = logging.getLogger('main')
    logger.setLevel(logging.DEBUG)
    handler = RotatingFileHandler('main.log')
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s %(name)s [%(levelname)s] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


def hello():
    for i in range(0, 10):
        print('hello world\n')
        time.sleep(0.5)


def main():
    logger = setup_logging()

    logger.debug('run main')
    if len(sys.argv) == 2:
        command = sys.argv[1]
    else:
        print('Usage: start/stop/restart/check')
        return
    config = {
        'command': command,
        # uncomment and set if you want
        # 'pid_file': '/var/run/dae.pid',
        # 'log_file': '/var/log/dae.log',
    }
    dae.daemon_exec(config)
    logger.debug('after daemon_exec')


if __name__ == '__main__':
    main()
    hello()
