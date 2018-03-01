class General(Exception):
    pass


class SpecificOne(General):
    pass


class SpecificTwo(General):
    pass


def raiser0():
    raise General()


def raiser1():
    raise SpecificOne()


def raiser2():
    raise SpecificTwo()


if __name__ == '__main__':
    for func in (raiser0, raiser1, raiser2):
        try:
            func()
        except General:
            import sys
            print('caught:', sys.exc_info()[0])
            print('---', sys.exc_info())
