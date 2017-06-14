import pickle
import shelve

from pizzashop import PizzaShop


def test_pickle_dump():
    obj = PizzaShop()
    db = open('pi_shop_db', 'wb')
    pickle.dump(obj, db)
    db.close()


def test_pickle_load():
    db = open('pi_shop_db', 'rb')
    obj = pickle.load(db)
    print(obj)
    db.close()


def test_shelve_save():
    obj = PizzaShop()
    db = shelve.open('sh_shop_db')
    db['shop'] = obj
    db.close()


def test_shelve_show():
    db = shelve.open('sh_shop_db')
    obj = db['shop']
    print(obj)
    db.close()


def test():
    # test_pickle_dump()
    # test_pickle_load()
    test_shelve_save()
    test_shelve_show()


if __name__ == '__main__':
    test()
