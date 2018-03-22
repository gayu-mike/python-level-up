import sys
import subprocess

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QThread
from PyQt5.QtNetwork import QUdpSocket
from PyQt5.QtNetwork import QHostAddress
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel


def log(*args, **kwargs):
    with open('log.txt', 'w') as f:
        f.write(*args, **kwargs)


class Worker(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        # print('click vpn')
        subprocess.run(['sudo', './cli', 'client.ovpn'])


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.mouse_pressed = False
        self.game_addr = ''
        self.udp_socket = QUdpSocket(self)
        self.resize(300, 500)

        self.window_layout = QVBoxLayout()
        self.title_layout = QHBoxLayout()
        self.content_layout = QVBoxLayout()

        self.title_widget = QWidget()
        self.content_widget = QWidget()

        self.logo_label = QLabel('赛博加速器')
        self.min_btn = QPushButton('最小化')
        self.close_btn = QPushButton('关闭')

        self.game_label = QLabel('游戏名称')
        self.add_btn = QPushButton('添加游戏')
        self.start_btn = QPushButton('开始加速')
        #TODO: 要在这里创建 worker 在函数中初始化会崩溃
        self.thread = Worker()
        self.vpn_btn = QPushButton('启动VPN')

        self.set_layout()
        self.bind_action()

    def set_layout(self):
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.title_layout.addWidget(self.logo_label)
        self.title_layout.addWidget(self.min_btn)
        self.title_layout.addWidget(self.close_btn)

        self.content_layout.addWidget(self.game_label, 1,
                                      Qt.AlignJustify | Qt.AlignVCenter)
        self.content_layout.addWidget(self.add_btn, 3,
                                      Qt.AlignJustify | Qt.AlignVCenter)
        self.content_layout.addWidget(self.start_btn, 1,
                                      Qt.AlignJustify | Qt.AlignVCenter)
        self.content_layout.addWidget(self.vpn_btn, 1,
                                      Qt.AlignJustify | Qt.AlignVCenter)

        self.title_widget.setLayout(self.title_layout)
        self.content_widget.setLayout(self.content_layout)

        self.window_layout.addWidget(self.title_widget, 1)
        self.window_layout.addWidget(self.content_widget, 7)
        self.setLayout(self.window_layout)

    def bind_action(self):
        self.min_btn.clicked.connect(self.showMinimized)
        self.close_btn.clicked.connect(QCoreApplication.instance().quit)
        self.add_btn.clicked.connect(self.click_add_btn)
        self.start_btn.clicked.connect(self.click_start_btn)
        self.vpn_btn.clicked.connect(self.click_vpn_btn)

    def click_add_btn(self):
        #TODO: host, port
        ip, ok = QInputDialog.getText(self, '选择游戏', 'ip')
        if ok:
            self.add_game(ip)

    def add_game(self, ip):
        """ 把游戏ip添加到主窗口
        应该用一个变量存储地址以便加速事件启用
        """
        self.game_addr = ip
        self.game_label.setText(ip)

    def click_start_btn(self):
        """ 加速，建立网络链接 """
        if self.game_addr:
            print(self.game_addr)
        #TODO: 获取 host, port
        self.udp_socket.writeDatagram(b'this is sb2', QHostAddress('192.168.8.108'), 8888)

    def click_vpn_btn(self):
        self.thread.start()

    def mousePressEvent(self, event):
        if not self.mouse_pressed:
            self.mouse_pressed = True
        if event.button() == Qt.LeftButton:
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
