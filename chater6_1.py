class Adder:

    def __init__(self, data):
        self.data = data


class ListAdder(Adder):

    def __add__(self, other):
        return self.data + other


class DictAdder(Adder):

    def __add__(self, other):
        for k, v in other.items():
            self.data[k] = v
        return self.data


def test_one():
    a = Adder()
    la = ListAdder()
    ld = DictAdder()

    a.add(1, 2)
    la.add([], [1, 2])
    ld.add({'a': 1}, {'b': 2, 'a': 2})
    la.add(1, 1)
    ld.add([], [])


def test_two():
    a = Adder(1)
    la = ListAdder([1])
    ld = DictAdder({'a': 1})

    # print(a + 2)
    print(la + [1, 2])
    print(ld + {'b': 2, 'a': 2})
    # la + 1
    # ld + []


def test():
    # test_one()
    test_two()


if __name__ == '__main__':
    test()
