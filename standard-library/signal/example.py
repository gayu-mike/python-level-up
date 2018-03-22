import os
import signal
import threading
import time


def func():
    while True:
        time.sleep(3)
        print('1111')


t = threading.Thread(target=func)
t.start()
time.sleep(6)
pid = os.getpid()
os.kill(pid, signal.SIGINT)
