class Person:
    def __init__(self, name, job=None, pay=0):
        """构造函数: 初始化实例的时候自动运行"""
        self.name = name
        self.job = job
        self.pay = pay

    def __str__(self):
        """print 运算符的重载"""
        return '[Person: %s, %s]' % (self.name, self.__dict__)
    
    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))


def test():
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    for p in [bob, sue]:
        print(p.pay)
        p.give_raise(.1)
        print(p.last_name(), p.pay)

    assert bob.name == 'Bob Smith'
    assert bob.job is None
    assert sue.job == 'dev'
    assert sue.pay == 110000


if __name__ == '__main__':
    test()
