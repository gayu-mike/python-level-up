import sys
import time


timefunc = time.clock if sys.platform[:3] == 'win' else time.time


def trace(*args):
    print(args)


def timer(func, *args, _repeat=1000, **kwargs):
    trace(func, args, kwargs, _repeat)
    start = timefunc()
    for i in range(_repeat):
        result = func(*args, **kwargs)
    spend = timefunc() - start
    return spend, result


def best(func, *args, **kwargs):
    _repeat = kwargs.pop('_repeat', 50)
    best = 2 ** 32
    for i in range(_repeat):
        time, result = timer(func, *args, _repeat=1, **kwargs)
        if time < best:
            best = time
    return best, result


def only_time(*args, **kwargs):
    spend, __ = timer(*args, **kwargs)
    return spend
