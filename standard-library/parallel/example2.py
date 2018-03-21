import time
from threading import Thread, Event


def countdown(started):
    time.sleep(4)
    started.set()
    print('countdown started.')


started = Event()

print('Launch countdown.')
t = Thread(target=countdown, args=(started,))
t.start()

# wait() will block main thread until set() is called.
started.wait()
print('countdown is running.')
