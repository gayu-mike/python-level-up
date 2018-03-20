.. _python-guide:

Python漫游指南略读
================

--------------
Python 开发环境
--------------

开始写代码之前, 要配置好 Python 的开发环境.

~~~~~~~~~~~~
Python 2 / 3
~~~~~~~~~~~~

Python 2 / 3 的现状是: 

- 目前大部分生产环境中的 Python 代码都是 2.7, 但到 2020 年 Python2 就会被弃用.
- Python3 已经可以运用到生产环境中.

所以总的来说, 从 Python3 入手学习, 在新项目中使用 Python3 , 都是非常好的选择.
但考虑到工作中绝大多数存在的项目都是 Python2.7, 以及如果开发一个开源项目要考虑众多
Python2 的使用者, 要学会兼容 Python2.7 .

.. note::
    另外看看下面3个链接:

    - `我的项目中可以使用Python3吗? <https://caniusepython3.com/>`_
    - `更多 <https://wiki.python.org/moin/Python2orPython3>`_
    - `写2/3兼容的代码 <https://docs.python.org/3/howto/pyporting.html>`_

当我们谈到Python的时候, 不仅仅指代码本身, 还指Python的实现(我的粗略理解是解释器和库): 

- CPython
- PyPy
- Jython
- IronPython
- PythonNet

于是我们选择安装CPython, 并且从上文可知, 我们讨论安装Python3.


~~~~~
编辑器
~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~
pipenv / pip / virtualenv
~~~~~~~~~~~~~~~~~~~~~~~~~

--------
好好写代码
--------

-------
应用场景
-------
