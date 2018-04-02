import logging
import random
import threading
import time

from logger import setup_logging


class Counter(object):
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        self.value += 1
        # logging.debug('Wait for lock...')
        # # self.lock.acquire()
        # try:
        #     self.value += 1
        # finally:
        #     # self.lock.release()
        #     logging.debug('value increased...')


def worker(c):
    for i in range(100):
        pause = random.random()
        # logging.debug('Sleep {:n}'.format(pause))
        time.sleep(pause)
        c.increment()
    # logging.debug('End...')


def main():
    setup_logging()
    # two threads use one counter
    # if they accidentally increase value at the same time
    # one may missed
    c = Counter()
    for i in range(10000):
        t = threading.Thread(target=worker, args=(c,), daemon=True)
        t.start()

    logging.debug('Start')
    main_thread = threading.main_thread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()
    logging.debug('Counter: {}'.format(c.value))


if __name__ == '__main__':
    main()
