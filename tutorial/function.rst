

lambda
------

.. code-block:: python3

    def sum(a, b):
        return a + b

    def sum(a, b): return a + b

    sum = lambda a, b: a + b

上面三个, 第一种是最常见的函数定义方式, 也很符合一般Python程序的风格.
第二个写法是被允许的, 解释器能理解, 但不Pythonic.
lambda看起来更像第二种, 实际上三者效果相同.
因为无论我们用那种方式定义, 都可以通过 ``sum(1, 2)`` 这样的方式来调用.

这样我们不难看出, 其实lambda也很容易理解, 我们可以把lambda赋值给一个变量,
那么这个变量就是一个函数, Python的def语句也是这么做的--把函数绑定到def后面的
变量名. lambda后面的变量是行参, :后面是表达式, 可以相当于return这么一个表达式.

这么看来完全可以把任何lambda改写成, nest function的形式, 我认为应该是完全可以这么做的.
lambda与之唯一不同的是, *不需要给它绑定一个变量名, 所以它才被称之为所谓的“匿名函数”.*

.. code-block:: python3

    >>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (2, 'apple')]
    >>> pairs.sort()
    >>> pairs
    [(1, 'one'), (2, 'ab'), (2, 'two'), (3, 'three'), (4, 'four')]
    >>> pairs.sort(key=lambda x: x[1])
    >>> pairs
    [(2, 'ab'), (4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

这里key接受一个callable, 当然也可以这样:

.. code-block:: python3

    def key(x):
        return x[1]

    >>> pairs.sort(key=key)

再次证明, lambda在实际使用上并没有什么特别, 只不过也算是一种更简短的写法.

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
    “隐藏”, 可能导致难以debug.
    
    Instagram在Pycon中提到, 使用annotations来避免上面这个问题.


