import threading
import time


def alert(msg):
    time.sleep(5)
    print('Alert: {}'.format(msg))


t = threading.Thread(target=alert, args=('now!',))
t.start()
print('Started.')
t.join()
print('Wait for child thread.')


class Alert(threading.Thread):
    def __init__(self, msg):
        threading.Thread.__init__()
        self.msg = msg

    def run(self):
        print('Alert: {}'.format(self.msg))


a = Alert('not now!')
a.start()
if a.is_alive:
    print('Started.')
a.join()
