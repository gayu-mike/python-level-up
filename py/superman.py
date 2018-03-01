# /usr/bin/env python3


class Super:
    def method(self):
        print('In Super.method')

    def delegate(self):
        """
        >>> Inheritor().delegate()
        AttributeError: Inheritor instance has no attribute 'action'
        """
        self.action()

    def delegate2(self):
        self.action2()

    def delegate3(self):
        self.action3()

    def action2(self):
        """assert 随后的判断如果为 False 就执行第二个参数语句"""
        assert False, 'action2 must be defined'

    def action3(self):
        raise NotImplementedError('action3 must be defined')


class Inheritor(Super):
    pass


class Replacer(Super):
    def method(self):
        print('In Replacer.method')


class Extender(Super):
    def method(self):
        print('Extender roll out')
        Super.method(self)


class Provider(Super):
    def action(self):
        print('Provider action')

    def action2(self):
        print('Provider action2')

    def action3(self):
        print('Provider action3')


def test_method():
    for c in (Inheritor, Replacer, Extender, Provider):
        print('\n%s...' % c.__name__)
        c().method()

def test_abstract():
    """抽象超类"""
    i = Inheritor()
    p = Provider()

    # p.delegate()
    # i.delegate()

    # p.delegate2()
    i.delegate2()

    # p.delegate3()
    # i.delegate3()


def test():
    test_method()
    test_abstract()


if __name__ == '__main__':
    test()
