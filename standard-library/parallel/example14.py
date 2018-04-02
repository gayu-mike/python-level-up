import logging
import threading
import time

from logger import setup_logging


def worker(e):
    logging.debug('Start worker..')
    open('test.txt', 'w')
    time.sleep(5)
    if e.is_set():
        return


def main():
    setup_logging()
    e = threading.Event()
    t = threading.Thread(target=worker, args=(e,))
    t.start()
    logging.debug('is alive {}'.format(t.is_alive()))
    # e.set()
    time.sleep(11)
    logging.debug('is alive {}'.format(t.is_alive()))


if __name__ == '__main__':
    main()
