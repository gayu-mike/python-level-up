Rapid GUI Programming With PyQt
===============================

----
前言
----

PyQt 的文档有所有类的 API，这本书介绍了如何使用它们来编程。  最初我使用 SWIG 来绑定 
 Python 和 Qt，我的目的是用 C++ 写的 Qt 代码可以用更 Pythonic 的形式实现。  于是我 
造了 SIP ，它是一个代码生成器，你能用 C++ 写的 Qt 程序都能用 Python 实现。  现在 
 PyQt 已经相对稳定，未来几年都会持续跟进 Qt 的发行。
    PyQt 的作者 Phil Thompson 2007

----
简介
----

本书讲解如何使用 Qt 和 Python 进行 GUI 编程。前置知识 
    - 懂一门 OOP 语言
    - 数据库部分需要一点数据库知识
    - 富文本部分需要一点 HTML 知识
    - 多线程部分需要一点多线程知识

使用 Python 不需要编译，使用 Qt 可移植到各个平台。因此只需要预安装 Python 解释器和 
PyQt 包就可以运行程序。  所以非常适合快速原型，同样也适合使用在生产环境。  在实际编程 
中，几乎总是有多种解决方案，API 和文档很少告诉你在什么场景下使用何种方案，本书提供 
场景的说明，也会解释不同方案的优劣。  PyQt 应用范围很广，代码量也从少至几十行多至 
十万行。 总的来说，PyQt4 由 10 个 Python 模块、400 个类、600 个方法组成.

~~~~~~~
本书结构
~~~~~~~

第一部分讲 Python，有经验的人可以只读一下 `QString`（第一章） 和 partial 
programming（第二章）。

第二部分讲 GUI 编程的基本概念，包括 Qt 的信号/槽、布局、控件、对话框、主窗口、 
Qt Designer、如何保存数据。

读完前 6 章就能掌握基本的 Python 和 PyQt 了 
第 7 章介绍 Qt Designer 
第 8 章讲文件系统，至少要读前 3 部分 
第 10 章至少读第一部分，第 11 章读完，它们讲解事件机制.


-----------
Python 基础
-----------

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Bytestrings, Unicode Strings, QStrings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

qstring 已过时.

partial function app at page 63.

    _code-block::python
        def partial(func, arg):
            def call():
                return func(arg)
            return call

--------------
基本的 GUI 编程
--------------

~~~~~~~~~~~~
介绍 GUI 编程
~~~~~~~~~~~~

^^^^^^^^^^^^^^^
signals / slots
^^^^^^^^^^^^^^^

注册一个 signal 的方式如下, 注意: **要作为类属性, 而不要作为实例属性.** 
信号函数的定义有点类似 C 的函数声明, `()` 表示空, 如果接受参数, 就要定义
参数类型 `()`.

.. _code-block:: python

    from PyQt5.QtCore import pyqtSignal, pyqtSlot

    class Form(QDialog):
        sig1 = pyqtSignal()
        sig2 = pyqtSignal(int)
        sig3 = pyqtSignal(str, list)

slot 可以是任何的 callable(比如普通的 python 函数). 所以列出以下两种形式, 
(接上面)

.. _code-block:: python

    @pyqtSlot(int)
    def slot1(self, val):
        return val

    def slot2(self, s, li):
        return s.join(li)

~~~~~
对话框
~~~~~

~~~~~
主窗口
~~~~~

使用 Qt Designer
~~~~~~~~~~~~~~~~

数据和自定义文件格式
~~~~~~~~~~~~~~~~~

GUI 编程进阶
-----------

布局和多文档
~~~~~~~~~~

事件, Clipboard, Drag and Drop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

自定义控件
~~~~~~~~~

Item-Based Graphics
~~~~~~~~~~~~~~~~~~~

富文本和打印
~~~~~~~~~~

Model / View Programming
~~~~~~~~~~~~~~~~~~~~~~~~

数据库
~~~~~

高阶 GUI 编程
------------

高阶 MV 模式
~~~~~~~~~~~

在线帮助和国际化
~~~~~~~~~~~~~~

网络
~~~~

多线程
~~~~~~

附录 A 安装
~~~~~~~~~~

附录 B 选择 PyQt 控件
~~~~~~~~~~~~~~~~~~~~

附录 C 选择的 PyQt 类继承树
~~~~~~~~~~~~~~~~~~~~~~~~~