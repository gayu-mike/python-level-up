# [DEBUG] (Thread-1  ) start 0.5
# [DEBUG] (Thread-2  ) start 0.4
# [DEBUG] (Thread-3  ) start 0.4
# [DEBUG] (MainThread) Joining Thread-1: alive? True
# [DEBUG] (Thread-3  ) stop
# [DEBUG] (Thread-2  ) stop
# [DEBUG] (Thread-1  ) stop
# [DEBUG] (MainThread) Joining Thread-2: alive? False
# [DEBUG] (MainThread) Joining Thread-3: alive? False

import logging
import random
import threading
import time


def worker():
    pause = random.randint(1, 5) / 10
    logging.debug('start {:.2n}'.format(pause))
    time.sleep(pause)
    logging.debug('stop')


def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(levelname)s] (%(threadName)-10s) %(message)s',
    )


def main():
    setup_logging()
    for i in range(3):
        t = threading.Thread(target=worker, daemon=True)
        t.start()

    main_thread = threading.main_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        logging.debug('Joining {0}: alive? {1}'
                      .format(t.getName(), t.is_alive()))
        t.join()


if __name__ == '__main__':
    main()
