class Squares:
    """One iter"""
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2


class S:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        """Return new S object supports multiple iters"""
        return S(self.value, self.stop)

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2


class It:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2


class Sq:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return It(self.value, self.stop)


class Iters:
    def __init__(self, value):
        self.value = value

    def __getitem__(self, i):
        print('get[%s]:' % i, end='')
        return self.value[i]

    def __iter__(self):
        print('iter=> ', end='')
        self.ix = 0
        return self

    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.value):
            raise StopIteration
        item = self.value[self.ix]
        self.ix += 1
        return item

    def __contains__(self, x):
        print('contains:', end='')
        return x in self.value
