from employee import Robot, Server


class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(self.name, 'orders from', server)

    def pay(self, server):
        print(self.name, 'pays for items to', server)


class Oven:
    def bake(self):
        print('oven bakes')


class PizzaShop:
    def __init__(self):
        self.server = Server('bob')
        self.chef = Robot('bran')
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

    def __repr__(self):
        return 'In PizzaShop: server=%s, chef=%s' % (self.server, self.chef)


def test():
    scene = PizzaShop()
    scene.order('homer')
    print('.' * 3)
    scene.order('shaggy')


if __name__ == '__main__':
    test()
