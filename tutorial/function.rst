.. _function:

Function
========

Function Defination
-------------------

有三种定义多个函数参数的方式, 可以组合:

- :ref:`默认参数 _<default>`
- :ref:`变长参数 _<arbitrary>`
- :ref:`关键字参数 _<keyword>`

.. _default:

默认参数
.......

.. code-block:: python3

    def func(a, b=2):
        return a ** b

    >>> func(2)
    2 ** 2
    >>> func(2, 3)
    2 ** 3

.. warning:: 默认参数只会初始化一次, 如果用可变的参数作为初始值, 会在每次调用的时候改变参数的值

.. code-block:: python3

    def apnd(a, L=[]):
        return L.append(a)

    >>> print(apnd(1))
    [1]
    >>> print(apnd(1))
    [1, 1]
    >>> print(apnd(1))
    [1, 1, 1]

如果想避免上述情况:

.. code-block:: python3

    def apnd(a, L=None):
        if L is None:
            L = []
        return L.append(a)

.. _arbitrary:

变长参数
.......

.. code-block:: python3

    def write_items(f, sep, *args):
        file.write(sep.join(args))

    >>> write_items(f, '/', 'included', 'in', 'args')
    'included/in/args'

其中, 当参数使用 `*` 的时候，args变量是一个tuple, 把余下的所有实参放在这个tuple 中.
args 后面还可以定义参数, 但必须是Keyword Arguments.

.. _keyword:

关键字参数
.........

.. code-block:: python3

    def write_items(f, *args, sep='/'):
        return sep.join(args)

    >>> write_items(f, 'all', 'in', 'args')
    'all/in/args'
    >>> write_items(f, 'all', 'in', 'args', sep=',')
    'all,in,args'

docstring
---------

去看看这个无聊的程序 ``docstring.py``, 这里直接给出一个标准的写法:

.. code-block:: python3

    def function():
        """ Short description.

        More details here.
        And the following lines uses
        the same indentation.
        """
        return

function annotations
--------------------

先看看这个例子:

.. code-block:: python3

    >>> def power(x: int, y: int = 2) -> int:
            return x ** y
    >>> power.__annotations__
    {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}
    >>> help(power)
    fun(x:int, y:int=2) -> int

这里我们可以看到, 函数有一个 ``__annotations__`` 的属性, 它是一个dict,
包含函数的参数、返回值. 定义annotations的方法是:

- parameter: 参数后加 `: 类型`
- return: 函数的 `()` 和 `:` 之间使用 `-> 类型`

.. note::
    其实这样的用法比较少见, 因为Python是一门动态语言(尽管这只是注释而不是限定类型).
    有时候遇到需要说明类型的情况下, 会在docstring中看到函数参数、变量、返回值的类型说明.
    但动态语言为人诟病的其中一点就是, 在所谓大型工程中, 动态类型不利于工程师阅读代码的时候明确
    一个函数接收什么类型. 有时候duck type并不会报错, 但实际传入的类型不正确, 这样就会把问题
    “隐藏”, 可能导致难以debug. Instagram在Pycon中提到, 使用annotations来避免上面这个问题.


