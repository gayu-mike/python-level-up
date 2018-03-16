def func1():
    """Do nothing.

    Hello
    world.
    """
    pass


def func2():
    """Do nothing.
    Hello
    world.
    """
    pass


def func3():
    """Do nothing.

        Hello
        world.
    """
    pass


def func4():
    """Do nothing.

    Hello
        world.
    """
    pass


def func5():
    """Do nothing.

        Hello
    world.
    """
    pass


print(func1.__doc__)
print()
print(func2.__doc__)
print()
print(func3.__doc__)
print()
print(func4.__doc__)
print()
print(func5.__doc__)
