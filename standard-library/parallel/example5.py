import logging
import threading
import time


def worker():
    logging.debug('start')
    time.sleep(0.2)
    logging.debug('stop')


def service():
    logging.debug('start')
    time.sleep(0.3)
    logging.debug('stop')


def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(levelname)s] (%(threadName)-10s) %(message)s',
    )


def main():
    setup_logging()
    s = threading.Thread(target=service, name='service')
    w = threading.Thread(target=worker, name='worker')
    t = threading.Thread(target=worker)
    s.start()
    w.start()
    t.start()


if __name__ == '__main__':
    main()
