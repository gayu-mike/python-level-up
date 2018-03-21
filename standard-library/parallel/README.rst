.. _parallel:

并发
===

**一个进程占有一个存储空间, 一个进程可以拥有多个线程, 线程共有这个存储空间.**

多线程
-----

多线程是共享数据和资源的(因为它们在同一块(进程的)内存区域, 共享寄存器/栈等资源),
先看例子:

.. code-block:: python3

    import threading

    def alert(msg):
        print('Alert: {}'.format(msg))

    t = threading.Thread(target=alert, args=('now!',))
    t.start()
    print('Started.')
    t.join()
    print('Wait for child thread.')

另一种写法(存在线程上下文的复杂问题, 暂时不使用):

.. code-block:: python3

    class Alert(threading.Thread):
        def __init__(self, msg):
            threading.Thread.__init__(self)
            self.msg = msg

        def run(self):
            print('Alert: {}'.format(self.msg))


    a = Alert('not now!')
    a.start()
    if a.is_alive:
        print('Started.')
    a.join()

除了 ``start`` / ``join`` 之外, 几乎不能对thread做更多的操作, 因为它是交由系统
运行的. 我们无法向它发送信号/主动结束/调度.

但是当我们想到使用多线程编程, 常常是因为有不止一个任务要处理, 比如要并行执行一个
阻塞的IO操作. 所以多线程编程有个核心问题就是协调线程的合作.

因此, 首先要了解如何在线程间通信.

尽管Python的Threading模块提供了一些解决同步优先级的方法: locks/events/condition
variables/semaphores. 但更易读易写的方法是使用Queue:

Queue是一个FIFO模型, 简单地使用list能展示这个模型:

.. code-block:: python3

    >>> queue = [1, 2, 3]
    >>> queue.append(4)
    >>> queue
    [1, 2, 3, 4]
    >>> queue.pop(0)
    1
    >>> queue
    [2, 3, 4]

.. note::
    实际中不要使用上面的写法, 因为list的实现让pop(0)这样的操作很慢, 应该使用
    ``collections.deque`` ``deque.leftpop()`` , 它的效率很高.

在清楚了FIFO模型之后, 我们使用 ``queue`` 模块来实现线程间通信:

.. code-block:: python3

    from queue import Queue
    from threading import Thread

    def producer(out_q):
        for i in range(4):
            out_q.put('hello')

    def consumer(in_q):
        while True:
            if not in_q.empty():
                msg = in_q.get()
                print(msg)
            else:
                print('no msg in queue')
                break

    q = Queue()
    p = Thread(target=producer, args=(q,))
    c = Thread(target=consumer, args=(q,))
    p.start()
    c.start()

可以看到, 两个线程共享同一个Queue对象, 这样就可以在不同线程间传递数据.
put/get方法使用起来类似前面例子的append/pop, 非常简单.