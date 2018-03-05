def async(func, args, *, callback):
    result = func(*args)
    callback(result)


def print_result(val):
    print(val)


def add(x, y):
    return x + y


if __name__ == '__main__':
    async(add, (2, 3), callback=print_result)
