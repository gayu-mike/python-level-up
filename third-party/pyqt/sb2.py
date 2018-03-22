# -*- coding: utf-8 -*-

from PyQt5 import QtCore
from PyQt5.QtCore import QThread
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtNetwork import QUdpSocket
from PyQt5.QtNetwork import QHostAddress
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QSize
# from PyQt5.QtGui import QPixmap


# CSS-like stylesheet setting
# window.setStyleSheet(STYLE_SHEET)
STYLE_SHEET = """
    QMainWindow {
        background-color: darkblue;
        border: 2px solid black;
    }
"""


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.mouse_pressed = False
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.game_addr = ''
        self.resize(293, 490)
        self.socket = QUdpSocket(self)

        #TODO: 布局在用绝对坐标
        self.label_logo = QLabel('LOGO', self)
        self.label_logo.move(20, 0)

        self.btn_add = QPushButton('添加游戏', self)
        self.btn_add.move(20, 20)
        self.btn_add.clicked.connect(self.show_games)

        self.label_addr = QLabel('游戏地址', self)
        self.label_addr.move(20, 50)

        self.btn_start = QPushButton('开始加速', self)
        self.btn_start.move(20, 100)
        self.btn_start.clicked.connect(self.start_accelerate)

        # self.setObjectName('btn_start')
        # self.render_btn_start()
        # self.center_btn_start(self.width(), self.height())

        # self.setObjectName("MainWindow")
        # self.setMenuBar(QtWidgets.QMenuBar())
        # self.centralWidget = QtWidgets.QWidget(self)
        # self.centralWidget.setObjectName("centralWidget")
        # self.setCentralWidget(self.centralWidget)
        # self.mainToolBar = QtWidgets.QToolBar(self)
        # self.mainToolBar.setObjectName("mainToolBar")
        # self.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        # self.statusBar = QtWidgets.QStatusBar(self)
        # self.statusBar.setObjectName("statusBar")
        # self.setStatusBar(self.statusBar)
        #
        # QtCore.QMetaObject.connectSlotsByName(self)

    def show_games(self):
        #TODO: host, port
        ip, ok = QInputDialog.getText(self, '选择游戏', 'ip')
        if ok:
            self.add_game(ip)

    def add_game(self, ip):
        """
        把游戏ip添加到主窗口
        应该用一个变量存储地址以便加速事件启用
        """
        self.game_addr = ip
        self.label_addr.setText(ip)

    def start_accelerate(self):
        """
        加速，建立网络链接
        """
        if self.game_addr:
            print(self.game_addr)
        #TODO: 获取 host, port
        self.socket.writeDatagram(b'this is sb2', QHostAddress('192.168.8.108'), 8888)


    def mousePressEvent(self, event):
        if not self.mouse_pressed:
            self.mouse_pressed = True
        if event.button() == QtCore.Qt.LeftButton:
            self.press_pos = event.pos()
            print('left')
            event.accept()

    def mouseMoveEvent(self, event):
        if self.mouse_pressed:
            self.move(event.globalPos() - self.press_pos)
            print('mouse move')
        event.accept()

    def mouseReleaseEvent(self, event):
        if self.mouse_pressed:
            self.mouse_pressed = False
        event.accept()

    def render_btn_start(self):
        # self.btn_start.setIcon(QIcon('start.png'))
        # self.btn_start.setIconSize(QSize(150, 150))
        # self.btn_start.setStyleSheet(btn_style)
        # self.btn_start.setFlat(True)
        print(self.btn_start.sizeHint())
        self.btn_start.show()

    def center_btn_start(self, w, h):
        self.btn_start.move((w-150)/2, 2*(h-150)/3)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())

