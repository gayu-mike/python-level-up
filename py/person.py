"""
Common pratice of OOP
"""

import shelve


class ModelHelper:
    def __repr__(self):
        """交互提示模式下的显示重载"""
        class_name = self.__class__.__name__
        a = ['{}: `{}`'.format(k, v) for k, v in self.__dict__.items()]
        attrs = '\n'.join(a)
        return '<class %s>\n%s' % (class_name, attrs)

    def _get_attrs(self):
        """单下划线开头一般就能避免被子类方法命名冲突"""
        attrs = ['{}={}'.format(k, getattr(self, k))
                 for k in sorted(self.__dict__)]
        return ', '.join(attrs)

    def __str__(self):
        formatter = '[{}> {}: {}]'.format(self.__class__.__bases__,
                                          self.__class__.__name__,
                                          self._get_attrs())
        return formatter

    def __private(self):
        """fake private: 强行访问只能通过 _ModelHelper__private 这样的方式"""
        print('You should not see this.')

    def save(self):
        """
        实例持久化的方法:
            keys have to be str and unique,
            values can be any Python objects.
        """
        db = shelve.open('persondb')
        db[self.name] = self
        db.close()


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
    def __init__(self, name, pay):
        Person.__init__(self, name, 'manager', pay)

    def give_raise(self, percent, bonus=0.10):
        # self.pay = int(self.pay * (1 + percent + bonus))
        Person.give_raise(self, percent + bonus)

    @staticmethod
    def scream():
        print('你把这个功能改一下，很简单的！')


class Developer(ModelHelper):
    """
    对象嵌入:
        这样基于嵌入的类，不会截获运算符重载方法
        如，需要重写 __str__ 否则打印会输出
        <__main__.Developer object at 0x103812278>
    """
    def __init__(self, name, pay):
        self.person = Person(name, 'developer', pay)

    def __getattr__(self, attr):
        return getattr(self.person, attr)


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def add_member(self, person):
        self.members.append(person)

    def show_all(self):
        for m in self.members:
            print(m)


def test_person():
    bob = Person('Bob Smith')
    print(bob)
    assert bob.name == 'Bob Smith'
    assert bob.job is None
    assert bob.pay is 0
    return bob


def test_manager():
    tom = Manager('Tom Clues', 50000)
    print(tom)
    assert tom.last_name() == 'Clues'
    tom.scream()
    Manager.scream()
    return tom


def test_developer():
    sue = Developer('Sue Jones', pay=100000)
    print(sue)
    assert sue.job == 'developer'
    return sue


def test_department():
    bob = test_person()
    tom = test_manager()
    sue = test_developer()
    print('{}{}{}'.format('-'*8, 'test_department', '-'*8))
    d = Department(bob, tom)
    d.show_all()
    d.add_member(sue)
    d.show_all()
    assert d.members == [bob, tom, sue]
    return bob, tom, sue


def test_save_and_update_ins():
    db = shelve.open('persondb')
    mike = db['Mike Zheng']
    pay = mike.pay
    mike.give_raise(0.2)
    assert mike.pay == pay * 1.2
    mike.save()


def test():
    # test_person()
    # test_manager()
    # test_developer()
    # test_department()
    test_save_and_update_ins()


mike = Developer('Mike Zheng', pay=5500)
mike.save()


if __name__ == '__main__':
    test()
