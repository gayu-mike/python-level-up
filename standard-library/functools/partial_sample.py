import functools


basetwo = functools.partial(int, base=2)


if __name__ == '__main__':
    print(basetwo('1010'))
