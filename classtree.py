def classtree(cls, indent):

    print('|' + '_' * indent + cls.__name__)
    for supercls in cls.__bases__:
        classtree(supercls, indent + 4)


def instancetree(ins):
    print('\nTree of %s' % ins)
    classtree(ins.__class__, 2)


def test():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B, C):
        pass

    class E:
        pass

    class F(D, E):
        pass

    instancetree(A())
    instancetree(B())
    instancetree(C())
    instancetree(D())
    instancetree(E())
    instancetree(F())


if __name__ == '__main__':
    test()
