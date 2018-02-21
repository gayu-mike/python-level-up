x = 11


def f():
    print(x)


def g():
    x = 22
    print(x)


class H:
    x = 33

    def i(self):
        x = 44
        self.x = 55


if __name__ == '__main__':
    print(x)  # 11
    f()  # 11
    # print(g.x)  # g has no attribute x
    g()  # 22
    print(x)  # 11 global x unchanged
    obj = H()
    print(obj.x)  # 33
    print(H.x)  # 33 same as obj.x
    obj.i()
    print(obj.x)  # 55
    print(H.x)  # 33
    # print(H.i.x)  # fail: only visible in method
