import logging
import threading
import time

from logger import setup_logging


def delay():
    logging.debug('Running delay function...')


def main():
    setup_logging()
    t1 = threading.Timer(1, delay)
    t1.setName('timer 1')
    t2 = threading.Timer(2, delay)
    t2.setName('timer 2')
    t3 = threading.Timer(5, delay)
    t1.start()
    t2.start()
    time.sleep(3)
    t3.cancel()


if __name__ == '__main__':
    main()
