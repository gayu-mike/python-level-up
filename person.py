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
        self.pay = int(self.pay * (1 + percent))


def test():
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    for p in [bob, sue]:
        print(p)
        p.give_raise(.1)

    assert bob.name == 'Bob Smith'
    assert bob.job is None
    assert sue.job == 'dev'
    assert sue.pay == 110000


if __name__ == '__main__':
    test()
