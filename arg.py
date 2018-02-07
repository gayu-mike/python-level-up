def adder(*args):
    result = args[0]
    for i in args[1:]:
        result += i
    print(result)
    return result

# adder(*(1, 2))
# adder(*'dfadfe')
# adder(*[4, 5, 5, 7])
# adder(*(1568, .454))
# adder(*{'a':1, 'b':2, 'c':3})


def fun2():
    fun1()


def fun1():
    print(1)


if __name__ == '__main__':
    fun2()
