

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

去看看这个无聊的程序 ``docstring.py``, 运行结果:

.. code-block:: python3

    Do nothing.

        Hello
        world.
        

    Do nothing.
        Hello
        world.
        

    Do nothing.

            Hello
            world.
        

    Do nothing.

        Hello
            world.
        

    Do nothing.

            Hello
        world.