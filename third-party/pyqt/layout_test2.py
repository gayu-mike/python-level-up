import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 500)

        self.window_layout = QVBoxLayout()
        self.title_layout = QHBoxLayout()
        self.content_layout = QVBoxLayout()

        self.title_widget = QWidget()
        self.content_widget = QWidget()

        self.logo_label = QLabel('赛博加速器')
        self.min_btn = QPushButton('最小化')
        self.close_btn = QPushButton('关闭')

        self.add_btn = QPushButton('添加游戏')
        self.start_btn = QPushButton('开始加速')

        self.set_layout()

    def set_layout(self):
        self.title_layout.addWidget(self.logo_label)
        self.title_layout.addWidget(self.min_btn)
        self.title_layout.addWidget(self.close_btn)

        self.content_layout.addWidget(self.add_btn, 3, Qt.AlignJustify | Qt.AlignVCenter)
        self.content_layout.addWidget(self.start_btn, 1, Qt.AlignJustify | Qt.AlignVCenter)

        self.title_widget.setLayout(self.title_layout)
        self.content_widget.setLayout(self.content_layout)

        self.window_layout.addWidget(self.title_widget, 1)
        self.window_layout.addWidget(self.content_widget, 7)
        self.setLayout(self.window_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

