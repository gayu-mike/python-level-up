import logging
import random
import threading
import time

from logger import setup_logging


class ThreadPool(object):
    def __init__(self):
        # super().__init__()
        self.active = []
        self.lock = threading.Lock()

    def activate(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug(f'<activate> Running {self.active}')

    def deactivate(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug(f'<deactivate> Running {self.active}')


def worker(s, pool):
    logging.debug('Joining to pool..')
    with s:
        name = threading.current_thread().getName()
        pool.activate(name)
        time.sleep(random.random())
        pool.deactivate(name)


def main():
    setup_logging()
    pool = ThreadPool()
    # At most two threads are running concurrently
    s = threading.Semaphore(2)
    for i in range(4):
        t = threading.Thread(target=worker, args=(s, pool))
        t.start()


if __name__ == '__main__':
    main()
