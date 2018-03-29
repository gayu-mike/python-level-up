import logging
import threading
import time


def worker():
    logging.debug('start')
    time.sleep(2)
    logging.debug('stop')


def service():
    logging.debug('start')
    time.sleep(3)
    logging.debug('stop')


def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(levelname)s] (%(threadName)-10s) %(message)s',
    )


def main():
    setup_logging()
    s = threading.Thread(target=service, name='service', daemon=True)
    w = threading.Thread(target=worker, name='worker')
    t = threading.Thread(target=worker)
    s.start()
    w.start()
    t.start()
    s.join(0.1)
    logging.debug(s.isAlive())
    s.join(3)
    logging.debug(s.is_alive())
    # w.join()


if __name__ == '__main__':
    main()
