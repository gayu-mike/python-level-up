#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, \
    with_statement

import logging
import os
import signal
import sys
import time


def to_bytes(s):
    if bytes != str:
        if type(s) == str:
            return s.encode()
    return s


def to_str(b):
    if str != bytes:
        if type(b) == bytes:
            return b.decode()
    return b


def daemon_exec(config):
    if os.name != 'posix':
        raise Exception('Daemon only works on Unix.')
    command = config.get('command')
    pid_file = config.get('pid_file', '/var/run/dae.pid')
    log_file = config.get('log_file', '/var/log/dae.log')

    if command == 'start':
        daemon_start(pid_file, log_file)
    elif command == 'stop':
        daemon_stop(pid_file)
        # exit or programming will still execute
        sys.exit(0)
    elif command == 'restart':
        daemon_restart(pid_file, log_file)
    elif command == 'check':
        daemon_check(pid_file)
    else:
        raise Exception('Unsupported command.')


def _write_pid_file(pid_file, pid):
    import fcntl
    import stat

    try:
        # refer to Unix open(2)
        # os.O_CREAT    optionally creat if not exist
        # os.RDWR       read and write
        # stat.S_IRUSR  00400 user has read permission
        # stat.S_IWUSR  00200 user has write permission
        fd = os.open(
            pid_file,
            os.O_RDWR | os.O_CREAT,
            stat.S_IRUSR | stat.S_IWUSR
        )
    except OSError as e:
        logging.error(e)
        return False

    # If the flags(FD_CLOEXEC) bit is set, the file
    # descriptor will automatically be closed after execve(2)
    flags = fcntl.fcntl(fd, fcntl.F_GETFD)
    assert flags != -1
    flags |= fcntl.FD_CLOEXEC
    r = fcntl.fcntl(fd, fcntl.F_SETFD, flags)
    assert r != -1

    try:
        # exclusive lock with non-blocking
        # starts from the beginning to the end of the file
        # len=0, start=0, whence=0(os.SEEK_SET)
        fcntl.lockf(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except IOError:
        buf = os.read(fd, 32)
        pid = to_str(buf)
        if r:
            logging.error('Already started at pid: {}'.format(pid))
        else:
            logging.error('Already started.')
        os.close(fd)
        return False

    # similar to file.write()
    os.ftruncate(fd, 0)
    os.write(fd, to_bytes(str(pid)))
    return True


def _remove_pid_file(pid_file):
    os.unlink(pid_file)


def freopen(f, mode, stream):
    newf = open(f, mode)
    newfd = newf.fileno()
    oldfd = stream.fileno()
    os.close(oldfd)
    # close oldfd and copy its fd to newfd
    os.dup2(newfd, oldfd)


def daemon_start(pid_file, log_file):

    def handle_exit(signum, _):
        if signum == signal.SIGTERM:
            sys.exit(0)
        sys.exit(1)

    # accpet two signals
    signal.signal(signal.SIGINT, handle_exit)
    signal.signal(signal.SIGTERM, handle_exit)

    # return twice: child(0) and parent(positive)
    pid = os.fork()
    assert pid != -1

    # wait for child to execute
    # stop executing parent's code
    if pid > 0:
        time.sleep(5)
        sys.exit(0)

    # 'real' ppid and pid
    ppid = os.getppid()
    pid = os.getpid()
    if _write_pid_file(pid_file, pid) is not True:
        os.kill(ppid, signal.SIGINT)
        sys.exit(1)

    # sid equals to child's pid
    os.setsid()
    signal.signal(signal.SIGHUP, signal.SIG_IGN)
    print('[{}] Started.'.format(pid))

    # since child move to another session
    # we can terminate parent
    os.kill(ppid, signal.SIGTERM)

    # redirect console stream
    sys.stdin.close()
    try:
        freopen(log_file, 'a', sys.stdout)
        freopen(log_file, 'a', sys.stderr)
    except IOError as e:
        logging.error(e)
        sys.exit(1)
    logging.debug('where am i?')


def daemon_stop(pid_file):
    import errno

    try:
        with open(pid_file) as f:
            pid = to_str(f.read())
            if not pid:
                logging.error('Not running.')
    except IOError as e:
        logging.error(e)
        # No such file or directory
        if e.errno == errno.ENOENT:
            logging.error('Not running.')
            return
        sys.exit(1)

    pid = int(pid)
    if pid > 0:
        try:
            os.kill(pid, signal.SIGTERM)
        except OSError as e:
            logging.error(e)
            # No such process
            if e.errno == errno.ESRCH:
                logging.error('Not running.')
                return
            sys.exit(1)
    else:
        logging.error('pid is negative: {}'.format(pid))

    # try to kill process with negative pid
    for i in range(0, 200):
        try:
            os.kill(pid, signal.SIG_DFL)
        except OSError as e:
            if e.errno == errno.ESRCH:
                break
        time.sleep(0.05)
    else:
        logging.error('Time out when stopping {}'.format(pid))
        sys.exit(1)

    print('[{}] Stopped.'.format(pid))
    _remove_pid_file(pid_file)


def daemon_restart(pid_file, log_file):
    daemon_stop(pid_file)
    daemon_start(pid_file, log_file)


def daemon_check(pid_file):
    pass
