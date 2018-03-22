"""
Using absolute layout
"""

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel


WINDOW_SIZE = (300, 500)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(*WINDOW_SIZE)

        self.logo_label = QLabel('赛博加速器')
        self.min_btn = QPushButton('最小化')
        self.close_btn = QPushButton('关闭')

        self.add_btn = QPushButton('添加游戏')
        self.start_btn = QPushButton('开始加速')

        # self.bind_widget()
        self.set_layout()

    def bind_widget(self):
        self.title_widget.addWidget(self.logo_label)
        self.title_layout.addWidget(self.min_btn)
        self.title_layout.addWidget(self.close_btn)

        self.window_layout.addLayout(self.title_layout, 1)
        self.window_layout.addStretch(1)
        self.window_layout.addWidget(self.add_btn, 4, Qt.AlignJustify | Qt.AlignVCenter)
        self.window_layout.addStretch(1)
        self.window_layout.addWidget(self.start_btn, 3, Qt.AlignJustify | Qt.AlignVCenter)

    def set_layout(self):
        self.close_btn.setGeometry(10, 10, 290, 0)
        self.setLayout()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

