class Spam:
    ins_num = 0

    def __init__(self):
        Spam.ins_num = Spam.ins_num + 1

    def print_num():
        """
        if call Spam.print_num()
        an unbound method should pass an instance like: Spam.print_num(self)
        if call self.print_num()
        it doesn't take any arguments but self was given
        """
        print('Number of instances:', Spam.ins_num)


def print_num():
    """
    calls pint_num() won't need class Egg or its instance
    but when you import Egg, you also need to import print_num
    """
    print('Number of instances:', Egg.ins_num)


class Egg:
    ins_num = 0

    def __init__(self):
        Egg.ins_num = Egg.ins_num + 1


#
# staticmethod and classmethod
#
# can be called both ways:
# SomeClass.meth()
# some_class_instance.meth()
class Ham:
    ins_num = 0

    def __init__(self):
        Ham.ins_num = Ham.ins_num + 1

    def print_num():
        print('Number of instances:', Ham.ins_num)
    print_num = staticmethod(print_num)


class Bur:
    ins_num = 0

    def __init__(self):
        Bur.ins_num = Bur.ins_num + 1

    def print_num(cls):
        print('Number of instances:', cls.ins_num)
    print_num = classmethod(print_num)


# finally...
class C:
    ins_num = 0

    def __init__(self):
        C.ins_num += 1

    @staticmethod
    def print_num():
        print('Number of instances:', C.ins_num)

    @classmethod
    def print_num2(cls):
        print('Number of instances:', cls.ins_num)


class D(C):
    ins_num = 0

    def __init__(self):
        D.ins_num += 1


if __name__ == '__main__':
    c = C()
    d1 = D()
    d2 = D()
    C.print_num()
    c.print_num()
    C.print_num2()
    c.print_num2()
    D.print_num()
    D.print_num2()
    d1.print_num()
    d2.print_num()
    d1.print_num2()
    d2.print_num2()
