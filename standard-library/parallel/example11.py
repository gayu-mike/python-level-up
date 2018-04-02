import logging
import threading
import time

from logger import setup_logging


def wait_for_event(e):
    """
    """
    logging.debug('wait_for_event starting...')
    logging.debug('event set: {}'.format(e.wait()))


def wait_for_event_timeout(e, t):
    """
    """
    logging.debug('wait_for_event_timeout starting...')
    while not e.is_set():
        logging.debug('wait_for_event_timeout starting...')
        is_set = e.wait(t)
        logging.debug('event set: {}'.format(is_set))
        if is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other work')


def main():
    setup_logging()
    e = threading.Event()
    t1 = threading.Thread(
        name='block',
        target=wait_for_event,
        args=(e,),
    )
    t2 = threading.Thread(
        name='non-block',
        target=wait_for_event_timeout,
        args=(e, 2),
    )
    t1.start()
    t2.start()

    logging.debug('Starting two threads...')
    time.sleep(4)
    e.set()
    logging.debug('Event set...')


if __name__ == '__main__':
    main()
