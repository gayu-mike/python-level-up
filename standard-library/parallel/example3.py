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
