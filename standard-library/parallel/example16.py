import logging
import socket
import threading
import time

from logger import setup_logging


class Counter(object):
    def __init__(self):
        self._running = True

    def stop(self):
        self._running = False

    def run(self, n):
        """ Pseudo Task

        A thread's task is sometimes a loop or so..
        Add an attribute and test it at the loop to determine
        whether to continue running the task..
        """
        while self._running and n > 0:
            logging.debug(f'Running {n}')
            n -= 1
            time.sleep(2)

    def listen(self, sock):
        sock.settimeout(1)
        while self._running:
            try:
                # A blocking I/O
                data = sock.recv(1024)
                logging.debug(f'Receive {data}')
                break
            except socket.timeout:
                logging.debug('time out...')
                continue
            else:
                sock.close()
        else:
            logging.debug('End of while loop...')
        return


def main():
    setup_logging()
    c = Counter()
    # t = threading.Thread(target=c.run, args=(10,))
    # t.start()
    # time.sleep(5)
    # c.stop()
    t = threading.Thread(target=c.listen, args=(socket.socket(),))
    t.start()
    time.sleep(5)
    c.stop()
    t.join()


if __name__ == '__main__':
    main()
