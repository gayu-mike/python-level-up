import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        ok = QPushButton('OK')
        cancel = QPushButton('Cancel')
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        hbox.addStretch(1)
        hbox.addWidget(ok)
        hbox.addWidget(cancel)

        # vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        # 没有下面的坐标无法使用box布局
        self.setGeometry(300, 300, 300, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())
