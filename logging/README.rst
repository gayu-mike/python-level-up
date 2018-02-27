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

*直到这里都还没提到上述 logging 的种种优点, 比如追踪 logging 自哪个 module , 需要看更高级的用法.*
