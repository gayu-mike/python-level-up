def func1():
    """Do nothing.

    Hello
    world.
    """
    pass


# Do nothing.
#
#     Hello
#     world.
print(func1.__doc__)


def func2():
    """Do nothing.
    Hello
    world.
    """
    pass


# Do nothing.
#     Hello
#     world.
print(func2.__doc__)


def func3():
    """Do nothing.

        Hello
        world.
    """
    pass


# Do nothing.
#
#         Hello
#         world.
print(func3.__doc__)


def func4():
    """Do nothing.

    Hello
        world.
    """
    pass


# Do nothing.
#
#     Hello
#         world.
print(func4.__doc__)


def func5():
    """Do nothing.

        Hello
    world.
    """
    pass


# Do nothing.

#         Hello
#     world.
print(func5.__doc__)
