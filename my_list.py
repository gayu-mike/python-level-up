class MyList:

    def __init__(self, data=[]):
        self.wrapper = [d for d in data]

    def __add__(self, other):
        return MyList(self.wrapper + other)

    def __mul__(self, times):
        return MyList(self.wrapper * times)

    def __getitem__(self, offset):
        return self.wrapper[offset]

    def __len__(self):
        return len(self.wrapper)

    def __getslice__(self, start, stop):
        return MyList(self.wrapper[start:stop])

    def append(self, other):
        self.wrapper.append(other)

    def __getattr__(self, name):
        return getattr(self.wrapper, name)

    def __repr__(self):
        return repr(self.wrapper)

    def count(self):
        count = 0
        for i in self.wrapper:
            if i:
                count += 1
        return count

    def __class__(self):
        return MyList

    def __contains__(self, other):
        result = False
        for w in self.wrapper:
            if w == other:
                result = True
        return result


if __name__ == '__main__':
    ml = MyList('spam')
    print(ml)
    print(ml[2])
    print(ml[1:])
    print(ml + ['eggs'])
    print(ml * 3)

    ml.append('a')
    print(ml)

    ml.sort()
    print(ml)

    for i in ml:
        print(i, end=' ')
