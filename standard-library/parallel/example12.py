import logging
import threading
import time

from logger import setup_logging


def wait_event(e):
    logging.debug('Starting.')
    # if wait(), block until event is set
    is_set = e.wait()
    logging.debug('is_set: {}'.format(is_set))


def wait_timeout(e, t):
    while not e.is_set():
        logging.debug('Starting..')
        # wait t time and continue processing
        is_set = e.wait(t)
        logging.debug('is_set: {}'.format(is_set))
        if is_set:
            logging.debug('Event is set...')
        else:
            logging.debug('Event is not set and processing other work..')


def main():
    setup_logging()
    e = threading.Event()
    we = threading.Thread(target=wait_event, name='block', args=(e,))
    wt = threading.Thread(target=wait_timeout, name='non-block', args=(e, 0.5))
    we.start()
    wt.start()

    logging.debug('Before Event.set()')
    time.sleep(2)
    e.set()
    logging.debug('Set...')


if __name__ == '__main__':
    main()
