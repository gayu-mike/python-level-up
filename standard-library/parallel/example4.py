import threading
import time


def worker():
    print('{} start.'.format(threading.current_thread().getName()))
    time.sleep(0.2)
    print('{} stop.'.format(threading.current_thread().getName()))


def service():
    print('{} start.'.format(threading.current_thread().getName()))
    time.sleep(0.3)
    print('{} stop.'.format(threading.current_thread().getName()))


def main():
    s = threading.Thread(target=service, name='service')
    w = threading.Thread(target=worker, name='worker')
    t = threading.Thread(target=worker)
    s.start()
    w.start()
    t.start()


if __name__ == '__main__':
    main()
