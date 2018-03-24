Sorting
=======

*原文出自: https://developers.google.com/edu/python/sorting*

-----------
list.sort()
-----------

``list.sort()`` 可以对列表进行排序, 它改变原来的列表对象中元素的顺序, 返回 ``None`` :

.. code-block:: python3

    >>> alist = [2, 3, 6, 4, 1]
    >>> print(alist.sort())
    None
    >>> print(alist)
    [1, 2, 3, 4, 6]

--------
sorted()
--------

``sorted()`` 是在 ``list.sort()`` 之后增加的内置方法:

.. code-block:: python3

    >>> help(sorted)
    sorted(iterable, /, *, key=None, reverse=False)
        Return a new list containing all items from the iterable in ascending order.

        A custom key function can be supplied to customize the sort order, and the
        reverse flag can be set to request the result in descending order.

用它来排序列表是很常见的, sorted()具有一下特性:

- 返回一个新的列表对象
- 不仅可以作用在列表上, 也可以用在任何可遍历的对象上
- 使用关键词参数 ``reverse=True`` 能倒序排列

下面的例子展示了这些特性:

.. code-block:: python3

    >>> a = [2, 3, 1, 5, 8, 4, 9]
    >>> print(sorted(a))
    [1, 2, 3, 4, 5, 8, 9]
    >>> print(a)
    [2, 3, 1, 5, 8, 4, 9]

    >>> d = {'a': 1, 'b': 2, 'c': 3}
    >>> print(sorted(d, reverse=True))
    ['c', 'b', 'a']
    >>> print(d)
    {'a': 1, 'b': 2, 'c': 3}

    >>> s = {'aa', 'BB', 'cc', 'DD'}
    >>> print(sorted(s))
    ['BB', 'DD', 'aa', 'cc']
    >>> print(s)
    {'BB', 'cc', 'DD', 'aa'}

~~~~~~~~~~~~~~~~~~~~~
使用 key= 自定义排序方式
~~~~~~~~~~~~~~~~~~~~~

另外, ``sorted()`` 很重要的一个特性是: 使用 ``key=callable`` 能实现更自定义化的排序,
比如, 上面例子中对s排序, 是大小写敏感的, 可以通过 ``str.lower()`` 来忽略大小写敏感.

.. code-block:: python3

    >>> s = {'aa', 'BB', 'cc', 'DD'}
    >>> print(sorted(s, key=str.lower))
    ['aa', 'BB', 'cc', 'DD']

那是因为, 在排序之前会对原来的对象中的元素逐一执行callable, 返回的proxy values和original 
values之间存在映射, sorted对proxy values排序, 再输出所映射的original values.

.. code-block:: python3

    >>> strs = ['ccc', 'aaaa', 'd', 'bb']
    >>> sorted(strs, key=len)
    # sorted([len('ccc'), len('aaaa'), len('d'), len('bb')])
    ['d', 'bb', 'ccc', 'aaaa']

所以, 只要是一个callable, 并且这个callable接收一个参数, 返回一个值, 那么就可以绑定到key=中,
这就给排序的方式提供了很大的灵活度. 比如
`自定义一个函数来实现自己想要的排序方式 <https://github.com/gayu-mike/python-level-up/tree/master/further-reading/sorting.py>`_

---
元组
---

.. code-block:: python3

    >>> t0 = ()
    >>> t1 = (1,)
    >>> t1 = 1,

------------------
list comprehension
------------------

list comprehension有时候可以让代码显得更简洁(并且比等价的for-loop效率更高):

.. code-block:: python3

    >>> nums = [1, 2, 3]
    >>> squares = [n * n for n in nums]
    >>> odd_squares = ['{}*{}={}'.format(n, n, n * n)
                       for n in nums if n % 2 != 0]

要看懂list comprehension, 只需要把for右边的看成控制流, 左边的看作return的值就可以了,
所以可以这样看上面的两条list comprehension:

.. code-block:: python3

    nums = [1, 2, 3]

    def sq(nums):
        result = []
        for n in nums:
            result.append(n * n)
        return result

    squares = sq(nums)

    def odd(nums):
        result = []
        for n in nums:
            if n % 2 != 0:
                result.append(n * n)
        return result

    odd_squares = odd(nums)
