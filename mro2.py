import inspect


class A(object):
    def __init__(self):
        print('This is A')

    def right(self):
        self.x = 'a'
        print('a')


class B(A):
    def __init__(self):
        print('Enter B')
        A.__init__(self)
        print('Leave B')

    def right(self):
        A.right(self)
        self.x = 'b'
        print(self.x)

class C(A):
    def __init__(self):
        print('Enter C')
        A.__init__(self)
        print('Leave C')

    def right(self):
        A.right(self)
        self.x = 'c'
        print(self.x)


class D(B, C):
    pass


D().right()
# print(inspect.getmro(D))
