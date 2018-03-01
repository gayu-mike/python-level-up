class TraceBlock:

    def message(self, arg):
        print('running', arg)

    def __enter__(self):
        print('starting WITH block')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is None:
            print('exited normally')
        else:
            print('raise an exception', exc_type)
            return False


if __name__ == '__main__':
    with TraceBlock() as t:
        t.message('test 1')
        print('reached')

    with TraceBlock() as t:
        t.message('test 2')
        raise TypeError
        print('not reached')
