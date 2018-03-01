import logging
import sys
import time

import dae


def hello():
    for i in range(0, 100):
        print('hello world\n')
        time.sleep(0.5)


def main():
    if len(sys.argv) == 2:
        command = sys.argv[1]
    else:
        print('Usage: start/stop/restart/check')
        return
    config = {
        'command': command,
        # uncomment and set if you want
        # 'pid_file': '/var/run/dae.pid',
        # 'log_file': '/var/log/dae.log',
    }
    dae.daemon_exec(config)


if __name__ == '__main__':
    main()
    hello()
