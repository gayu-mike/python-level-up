class ModelHelper:
    def __repr__(self):
        """交互提示模式下的显示重载"""
        class_name = self.__class__.__name__
        a = ['{}: `{}`'.format(k, v) for k, v in self.__dict__.items()]
        attrs = '\n'.join(a)
        return '<class %s>\n%s' % (class_name, attrs)


class Person(ModelHelper):
    def __init__(self, name, job=None, pay=0):
        """构造函数: 初始化实例的时候自动运行"""
        self.name = name
        self.job = job
        self.pay = pay

    def __str__(self):
        """print 运算符的重载"""
        return '[Person: %s, %s]' % (self.name, self.pay)
    
    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = round(self.pay * (1 + percent))


class Manager(Person):
    def give_raise(self, percent, bonus=0.10):
        # self.pay = int(self.pay * (1 + percent + bonus))
        Person.give_raise(self, percent + bonus)


def test_person():
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    for p in [bob, sue]:
        print(p)
        p.give_raise(0.10)

    assert bob.name == 'Bob Smith'
    assert bob.job is None
    assert sue.job == 'dev'
    assert sue.pay == 110000


def test_manager():
    tom = Manager('Tom Clues', 'mgr', 50000)
    tom.give_raise(0.05)
    print(tom)

    assert tom.last_name() == 'Clues'
    assert tom.pay == 57500


def test():
    # test_person()
    test_manager()


if __name__ == '__main__':
    test()
