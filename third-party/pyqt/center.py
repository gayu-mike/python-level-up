import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QWidget


def log(*args, **kwargs):
    print(*args, **kwargs)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('赛博')
        # set location
        self.resize(250, 150) # self.move(300, 300)
        # self.setGeometry(300, 300, 250, 150)
        self.center()

        self.show()

    def center(self):
        frame = self.frameGeometry()
        log(frame)
        screen_center = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(screen_center)
        # self.move(frame.topLeft())
        log('screen_center: ', screen_center)
        log('frame topleft: ', frame.topLeft())


if __name__ == '__main__':
    # 应用 instance
    app = QApplication(sys.argv)
    # 窗口控件
    w = Window()

    sys.exit(app.exec_())
