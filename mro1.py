import inspect


class A(object):
    def __init__(self):
        print('This is A')

    def right(self):
        self.x = 'a'
        print(self.x)


class B(A):
    def __init__(self):
        print('Enter B')
        super(B, self).__init__()
        print('Leave B')

    def right(self):
        super(B, self).right()
        self.x = 'b'
        print(self.x)


class C(A):
    def __init__(self):
        print('Enter C')
        super(C, self).__init__()
        print('Leave C')

    def right(self):
        super(C, self).right()
        self.x = 'c'
        print(self.x)


class D(B, C):
    pass


D().right()
# print(inspect.getmro(D))
