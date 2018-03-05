#! usr/bin/evn python3

""" A Python daemon
使用:
    把要执行的脚本放在下面的 `Worker.run()` 函数中, 任务的定时器修改 `time.sleep()` 中的参数即可.
命令:
    `python daemon.py start` 启动
    `python daemon.py stop` 终止
    `python daemon.py restart` 重启
    `python daemon.py check`
"""


import os
import signal
import sys
import time


class Daemon(object):
    """ A base daemon class
    Subclass and override run() to set your task.
    """

    def __init__(self):
        self.pid = None
        self.sid = None
        self.log_file = '/var/log/daemon.log'
        self.pid_file = '/var/run/daemon.pid'

    def daemonize(self):
        self.pid = os.fork()
        assert self.pid != -1

        # exit parent process
        if self.pid > 0:
            time.sleep(5)
            # pid turn to 0
            sys.exit(0)

        os.umask(0)

        self.sid = os.setsid()
        assert self.sid != -1
        # signal.signal(signal.SIGHUP, signal.SIGIGN)
        # os.chdir('/')

        self.pid = os.getpid()
        with open('daemon.pid', 'w+') as f:
            f.write(str(self.pid))

        sys.stdin.close()
        # sys.stdout.close()
        # sys.stderr.close()
        try:
            self.freopen(self.log_file, 'a', sys.stdout)
            self.freopen(self.log_file, 'a', sys.stderr)
        except IOError as e:
            print(e)

    def freopen(self, f, mode, stream):
        """ redirect log
        """
        newf = open(f, mode)
        newfd = newf.fileno()
        oldfd = stream.fileno()
        os.close(oldfd)
        os.dup2(newfd, oldfd)

    def start(self):
        try:
            p = open('daemon.pid', 'r')
            self.pid = int(p.read())
            p.close()
        except IOError:
            self.daemonize()
            self.run()
        else:
            print('Daemon already started.')

    def stop(self):
        try:
            with open('daemon.pid', 'r') as f:
                self.pid = int(f.read())
        except FileNotFoundError:
            print('PID file not exist.')
        else:
            os.remove('daemon.pid')
            try:
                os.kill(self.pid, signal.SIGTERM)
            except (IOError, OSError, ProcessLookupError):
                # print(e)
                print('Daemon not exist.')

    def restart(self):
        self.stop()
        self.start()

    def status(self):
        self.pid = self.get_pid()
        if self.pid:
            print('Daemon is running.')
            return True
        else:
            print('Daemon is not running.')
            return False

    def is_alive(self):
        return self.status()

    def get_pid(self):
        try:
            with open('daemon.pid', 'r') as f:
                return int(f.read())
        except IOError:
            return

    def run(self):
        """ Override """
        pass


class Worker(Daemon):

    def run(self):
        count = 0

        def log(count):
            with open('daemon.log', 'a+') as f:
                f.write('{}. hello world!\n'.format(count))
        while True:
            time.sleep(3)
            count += 1
            log()
            ##################
            # Your script here
            ##################

    def check(self):
        if not self.is_alive():
            self.restart()


def main():
    w = Worker()
    if os.name != 'posix':
        raise Exception('Daemon only works on Unix.')
    if len(sys.argv) == 2:
        command = sys.argv[1]
        if command == 'start':
            w.start()
        elif command == 'stop':
            w.stop()
        elif command == 'restart':
            w.restart()
        elif command == 'status':
            w.status()
        elif command == 'check':
            w.check()
    else:
        w.start()


if __name__ == '__main__':
    main()
