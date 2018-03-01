"""继承 list 实现的 set"""


class Set(list):

    def __init__(self, value=[]):
        list.__init__([])
        self.concat(value)

    def concat(self, value):
        for x in value:
            if x not in self:
                self.append(x)

    def intersect(self, other):
        res = []
        for x in other:
            if x in self:
                res.append(x)
        return Set(res)

    def union(self, other):
        res = self
        for x in other:
            if x not in self:
                res.append(x)
        return Set(res)

    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __add__(self, other):
        return self.__or__(other)

    def __radd__(self, other):
        return self.__add__(other, self)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        res = []
        for x in self:
            if x not in other:
                res.append(x)
        return Set(res)

    def __rsub__(self, other):
        return self.__sub__(other, self)

    def __repr__(self):
        return 'Set:' + list.__repr__(self)


if __name__ == '__main__':
    x = Set([1, 3, 3, 7, 5, 7])
    y = Set([1, 4, 7, 6, 4])
    print('x, y', (x, y))
    print('x intersect y', x.intersect(y))
    print('y union x', y.union(x))
    print('length of x, y', (len(x), len(y)))
    print('x[2]', x[2])
    for i in x:
        for j in y:
            print('for x, y', (i, j))
    print('x & y', (x & y))
    print('x | y', (x | y))
    print('x + y', (x + y))
    print('radd', (Set([2, 4, 5]) + x))
    x += Set([2, 3, 5])
    print('iadd', x)
    print('sub', (x - y))
    x -= Set([2, 3, 5])
    print('isub', x)
