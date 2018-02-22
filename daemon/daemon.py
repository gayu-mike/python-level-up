#! usr/bin/evn python3

""" A Python daemon
使用:
        把要执行的任务以函数的形式放在下面的 `task()` 函数中，
    任务的定时器修改 `time.sleep()` 中的参数即可。然后 `python daemon.py`
    启动该守护进程。
        如果要停止该守护进程，先 `ps axj | grep python` 找到改进程, 再 `kill` 即可。
"""


import os
# import signal
import sys
import time


class Daemon(object):
    def __init__(self):
        self.pid = None

    def daemonize(self):
        self.pid = os.fork()
        assert self.pid != -1
        # exit parent process
        if self.pid > 0:
            print('Exit parent process.')
            time.sleep(5)
            sys.exit(0)

        os.umask(0)

        sid = os.setsid()
        assert sid != -1
        # signal.signal(signal.SIGHUP, signal.SIGIGN)
        # os.chdir('/')

        with open('daemon.pid', 'w+') as f:
            f.write(str(self.pid))
        print('Start daemon pid: {}'.format(self.pid))

        sys.stdin.close()
        sys.stdout.close()
        sys.stderr.close()

    def start(self):
        try:
            p = open('daemon.pid', 'r')
            self.pid = int(p.read())
            print('Read daemon id: {}'.format(self.pid))
            p.close()
        except Exception as e:
            print(e)
            self.daemonize()
            self.run()

    def run(self):
        pass


class Worker(Daemon):
    def run(self):
        def log():
            with open('daemon.log', 'a+') as f:
                f.write('hello world!\n')
        while True:
            time.sleep(3)
            # Your script here
            log()


def main():
    w = Worker()
    w.start()


if __name__ == '__main__':
    main()
