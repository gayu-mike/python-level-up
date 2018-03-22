import sys
import time


from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtWidgets import QApplication, QLabel


app = QApplication(sys.argv)

# try:
#     due = QTime.currentTime()
#     msg = 'Alert!'
#     if len(sys.argv) < 2:
#         raise ValueError
#     hours, mins = sys.argv[1].split(':')
#     due = QTime(int(hours), int(mins))
#     if not due.isValid():
#         raise ValueError
#     if len(sys.argv) > 2:
#         msg = ''.join(sys.argv[2:])
# except ValueError:
#     msg = 'Usage: alert.pyw HH:MM'

# python alert.pyw 12:20 get up
hour, minute = sys.argv[1].split(':')
due = QTime(int(hour), int(minute))

msg = 'alert!!!'
if len(sys.argv) > 2:
    msg += ' '.join(sys.argv[2:])

while QTime.currentTime() < due:
    time.sleep(20)

# 把一个 label 当作 top-level-window
label = QLabel('<font color=red size=72><b>{}</b></font>'.format(msg))
label.setWindowFlags(Qt.SplashScreen)
label.show()

QTimer.singleShot(6000, app.quit)
app.exec_()
