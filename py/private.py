"""伪私有变量"""


# 不同类中使用同名属性, 如果被继承到一个子类.
# 会相互干扰.
class A:
    def meth1(self):
        self.x = 88

    def meth2(self):
        print(self.x)


class B:
    def meth3(self):
        self.x = 99

    def meth4(self):
        print(self.x)


class C(A, B):
    pass


# 如果使用 __x 这样的伪私有变量, 则不会.
class D:
    def metha(self):
        self.__x = 88

    def methb(self):
        print(self.__x)


class E:
    def methc(self):
        self.__x = 99

    def methd(self):
        print(self.__x)


class F(D, E):
    pass


def test_public():
    c = C()
    c.meth1()
    c.meth2()
    c.meth3()
    c.meth2()  # get 99 cause self.x binds to meth3's x
    c.meth1()
    c.meth4()


def test_private():
    f = F()
    f.metha()
    # f.methd()  # AttributeError: F instance has no attribute '_E__x'
    f.methc()
    f.methb()
    f.methd()
    print(f.__dict__)
    print(dir(f))


# 如果某个类倾向于混合到其他类中, 并且它的某个方法只在该类中使用,
# 也可以使用这种技巧.
class Super:
    def method(self):
        pass


class Tool:
    def __method(self):
        print('Tool.__method')

    def call_method(self):
        self.__method()


class Sub1(Tool, Super):
    def action(self):
        self.method()  # calls Super.method


class Sub2(Tool):
    def __init__(self):
        self.method = 99  # won't change Tool.__method
        self.__method = 100

    def show(self):
        print(self.method, self.__method)


def test_method():
    t = Tool()
    s2 = Sub2()
    s2.show()
    t.call_method()
    # 只要记住:
    # 在类的外部无法通过 __x 这种形式引用
    print(t._Tool__method)
    print(t.__method)


if __name__ == '__main__':
    # test_public()
    # test_private()
    test_method()
