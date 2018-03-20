Logging
=======

logging 部分的文档很难读, PEP282 简要地作了介绍, 另外文档中 basic logging tutorial 部分也相对好读.

vs Print
--------

和 print 大法相比的话, 好像所有知名的开源库都在用 logging 模块, 而自己魔改的 log 也有很多难以追踪的情况.
**print 在 python 中大概最适合发挥的地方就是 print 那些 user help/usage 信息**
话说到这里, 还是要在强调一下 logging 的好处:
    - log record 记录了相当多用来诊断的信息
    - 所有的 log 都会被包含到 root logger 里面
    - logging.Logger.setLever() 可以分层筛掉 log 信息, 还可以 logging.Logger.disabled 关掉 logging

*KR 也大概提了 lib / app 里面 logging 的用法和不同之处, 提到了 ini / json / code 三种方式设定 logging, 但我们先来看看 basic tutorial*

Basic Logging tutorial
----------------------

when to use
~~~~~~~~~~~

我们只讨论 python logging 里面的分级
    - debug     *顾名思义*
    - info      *常用来追踪一些程序中重要的数据, 确保它预期执行*
    - warning   *反馈一些不如预期的事, 或者即将到来的问题*
    - error     *程序中的某些功能可能不能执行*
    - critical  *程序可能要中断了*

log to screen and file
~~~~~~~~~~~~~~~~~~~~~~

看 :ref:`sample.py`_

from multi module
~~~~~~~~~~~~~~~~~

上面 logging 用起来和 print 差不多, 除了可以控制不同 level.
下面看看在不同 module 中 logging 的操作.
假设有 `main.py` `utils.py`::
    # utils.py
    import logging

    def func():
        logging.debug('do sth')

    # main.py
    import logging
    import utils

    def main():
        logging.basicConfig(filename='app.log', level.INFO)
        logging.info('start')
        utils.func()
        logging.info('stop')

    if __name__ == '__main__':
        main()

那么执行起来, 也跟普通的 print 差不多, 所有 log 都在同一个文件下, 你并不知道来自那个 module ::
    INFO:root:start
    DEBUG:root:do sth
    INFO:root:stop

var data
~~~~~~~~

:ref:`sample.py`_

format and datetime
~~~~~~~~~~~~~~~~~~~

:ref:`format_logging.py`_
在 LogRecord attributes 中有 logging 可以概括的属性. 

--------------------------

*直到这里都还没提到上述 logging 的种种优点, 比如追踪 logging 自哪个 module , 需要看更高级的用法.
在研究更高级的用法之前, 我们先看看 logging 在更实际的项目中如何使用.*

Advanced Logging
~~~~~~~~~~~~~~~~

- LogRecord
- logger
- handler
- filter
- formatter

logger
~~~~~~

作用: 生成 logrecord / 命名 / 选定初始级别 / 发送到 handler 

默认情况的 LogRecord 是这样格式的::
    WARNING:root:hello!

其中 `root` 就是命名, 命名可以通过::
    logger = logging.getLoger(__name__)
进行修改, 命名是继承的, 所以上面的代码会生成 `foo.bar.baz` 这样的名称. 

同样, 级别也是继承的. 因为所有的 logger 向上 propergate 之后最终到 root, 默认没设置的情况下 root 的级别是 `WARNING`.

    Logger.setLevel()
    Logger.addHandler() / Logger.removeHandler()
    Logger.addFilter() / removeFilter()

handler
~~~~~~~

决定收到的 LogRecord 的去向. 
设想一个场景, error 一下的 logrecord 发送到一个文件, error 以上的发送到 console, critical 的发送 email. 
这样的工作就是由 handler 负责的. 

它和 logger 的关系是 n 对 n , 例如原生提供的 handler 有 StreamHandler / FileHandler / RotatingFileHandler / NullHandler , 一个 logger 可以添加多个 handler, 多个 logger 可以使用同一个 handler. 

    setLevel()
    setFormatter()
    addFilter() / removeFilter()

filter
~~~~~~

虽然 logger / handler 都可以设置分级, 但仍然可以使用 filter attach 到上面这两个对象上, 它能提供更可定义的筛选. 

formatter
~~~~~~~~~

基本上就是用来格式化输出的. 

configure logging
-----------------

配置 logging 有三种方式
    - code
    - ini file
    - dict/json

code
~~~~

:ref:`foo.py` `bar.py`

INI file
~~~~~~~~

dict / json
~~~~~~~~~~~

Logging in a library
--------------------

logging 应该由用户(开发者)来使用, 所以在 library 中应该强调下面一点: 
**除了 NullHandler 之外, 不要使用任何 handler.**

KR 的建议是在包的 `__init__.py` 中使用::
    import logging
    logging.getLoger(__name__).addHandler(logging.NullHandler)

更完整的来自 requests 的例子如下::
    import logging
    try:  # Python 2.7+
        from logging import NullHandler
    except ImportError:
        class NullHandler(logging.Handler):
            def emit(self, record):
                pass

    logging.getLogger(__name__).addHandler(NullHandler())
