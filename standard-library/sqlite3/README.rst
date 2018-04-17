sqlite3
=======

**DB-API 2.0 interface for SQLite**

-------------------
Python 中的数据持久化
-------------------

我们平常写程序中保存变量等等, 都是在运行程序是保存在寄存器或者内存中的. 比如:

.. code-block:: python3

    x = 1

如果需要保存它, 我们可以写入文件, 下一次运行程序的时候读取.

再比如更复杂一点的情况, 使用面向对象来表达一个程序对象以及它的属性:

.. code-block:: python3

    class User(object):
        def __init__(self, username, password):
            self.username = username
            self.password = password

    user = User('foo', 'bar')

这样的写法都是很常遇到的, 但是程序中的代码只在运行时保存在内存中, 一旦程序结束就不复存在.
要想保留在硬盘中, 使用文件是一个方法, 比如使用 Python 的数据结构来表达上述对象:

.. code-block:: python3

    def save(data, path):
        s = json.dumps(data)
        with open(path, 'w+') as f:
            f.write(s)

    def load(path):
        with open(path) as f:
            s = f.read()
            return json.loads(s)

    class User(object):
        [...]

        @classmethod
        def assign(cls, d):
            m = User('foo', 'bar')
            for k, v in d.items():
                setattr(m, k, v)

        @classmethod
        def all(cls):
            path = 'test.db'
            data = load(path)
            all_ins = [cls.load(ins) for ins in data]
            return all_ins

同理, 可以把属性/数据用 Python 的数据结构来组织, 用任意文件, 任意格式存储.
(只要能够序列化/反序列化, 读/写)

-------
sqlite3
-------

数据库的存在, 为数据持久、管理数据化提供了许多方便.

主流的数据库管理系统如: MySQL / PostSQL / Oricle 等, 都是以服务的形式监听在一个端口的.
(C/S 模式) 也需要账号密码, 需要复杂的配置等.

`SQLite <https://www.sqlite.org/index.html>`_ 是一个单文件, 小巧的数据库系统.
Python 标准库中提供了 ``sqlite3`` 模块作为访问 SQLite 的接口.
