import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QToolTip
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox


def log(*args, **kwargs):
    print(*args, **kwargs)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        QToolTip.setFont(QFont('SansSerif', 10))
        self.initUI()

    def initUI(self):
        self.background('background.jpg')
        # button instance
        btn = QPushButton('Quit', self)
        # set title & icon & tips
        self.setWindowTitle('赛博')
        self.setWindowIcon(QIcon('icon.png'))
        self.setToolTip('This is <b>QWidget</b>')
        btn.setToolTip('This is <b>QButton</b>')
        # btn click
        btn.clicked.connect(
            QCoreApplication.instance().quit)
        btn.resize(btn.sizeHint())
        #
        btn.move(50, 50)

        # set location
        # self.resize(250, 150) # self.move(300, 300)
        self.setGeometry(300, 300, 250, 150)
        self.center()

        self.show()

    def background(self, path):
        pic = QPixmap(path)
        painter = QPainter()
        painter.begin(pic)
        painter.drawPixmap(300, 300, self.width(), self.height(), pic)
        painter.end()

    def bgi(self):
        # self.setStyleSheet("background-image: 'icon.png'")
        img = QImage('icon.png').scaled(250, 150)
        palette = QPalette()
        palette.setBrush(10, QBrush(img))
        self.setPalette(palette)

    def center(self):
        frame = self.frameGeometry()
        log(frame)
        screen_center = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(screen_center)
        self.move(frame.topLeft())
        log('screen_center: ', screen_center)
        log('frame topleft: ', frame.topLeft())

    def closeEvent(self, event):
        """重写默认的x关闭按钮"""
        reply = QMessageBox.question(self, 'Message', 'Sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    # 应用 instance
    app = QApplication(sys.argv)
    # 窗口控件
    w = Window()

    sys.exit(app.exec_())
