class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def give_raise(self, percent):
        self.salary *= 1 + percent

    def work(self):
        print(self.name, 'does stuff')

    def __repr__(self):
        return '<Employee: name=%s, salary=%s>' % (self.name, self.salary)


class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)

    def work(self):
        print(self.name, 'makes food')


class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)

    def work(self):
        print(self.name, 'interfaces with customers')


class Robot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)

    def work(self):
        print(self.name, 'makes pizza')


def test():
    bob = Robot('bob')
    print(bob)
    bob.work()
    bob.give_raise(0.20)
    print(bob)
    print()

    for e in (Employee, Chef, Server, Robot):
        obj = e(e.__name__)
        obj.work()


if __name__ == '__main__':
    test()
