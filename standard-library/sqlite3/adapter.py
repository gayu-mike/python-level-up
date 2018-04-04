import sqlite3


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __conform__(self, protocol):
        """ Convert data type """
        if protocol is sqlite3.PrepareProtocol:
            return '{};{}'.format(self.x, self.y)


class Point2(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def adapt_poit(p):
    return '{};{}'.format(p.x, p.y)


conn = sqlite3.connect(':memory:')
c = conn.cursor()

# Adapt in class.__conform__
p = Point(4.0, -3.2)
c.execute('SELECT ?', (p,))
print(c.fetchall())

# Adapt as a registered callable
sqlite3.register_adapter(Point2, adapt_poit)
p = Point2(4.0, -3.2)
c.execute('SELECT ?', (p,))
print(c.fetchall())
