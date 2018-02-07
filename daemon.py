""" A Python daemon

Usage:
        Put your script/function at `task()`, as shows below,
    set timer by overwriting `time.sleep()`.  Then run
    `python daemon.py`.
        If you want to stop the daemon, run
    `killall python daemon.py` in your terminal.
(使用)
        把要执行的任务以函数的形式放在下面的 `task()` 函数中，
    任务的定时器修改 `time.sleep()` 中的参数即可。然后 `python daemon.py`
    启动该守护进程。
        如果要停止该守护进程，目前，只需 `killall python daemon.py` 即可。
"""

import os
import signal
import sys
import time


def task():
    time.sleep(3)
    # Your script here


def daemonize():
    pid = os.fork()
    assert pid != -1

    if pid > 0:
        time.sleep(5)
        sys.exit(0)

    os.umask(0)

    sid = os.setsid()
    assert sid != -1
    # signal.signal(signal.SIGHUP, signal.SIGIGN)

    # os.chdir('/')

    sys.stdin.close()
    sys.stdout.close()
    sys.stderr.close()
    while True:
        task()


if __name__ == '__main__':
    daemonize()
