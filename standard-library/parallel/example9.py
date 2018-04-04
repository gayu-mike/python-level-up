import logging
import threading


class SubThread(threading.Thread):
    def run(self):
        logging.debug('SubThread... {}'.format(self._args))


class ThreadWithArg(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.args = args
        self.kwargs = kwargs

    def run(self):
        logging.debug('Running with {} and {}'.format(self.args, self.kwargs))


def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(levelname)s] (%(threadName)-10s) %(message)s',
    )


def alert(msg):
    print('Alert: {}'.format(msg))


def main():
    setup_logging()
    st = SubThread(target=alert, args=('Now!',))
    st.start()
    for i in range(3):
        t = ThreadWithArg(i, a='a', b='b')
        t.start()


if __name__ == '__main__':
    main()
