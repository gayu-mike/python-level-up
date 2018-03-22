import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # grid = QGridLayout()
        # self.setLayout(grid)
        # btns = [QPushButton('button{}'.format(i)) for i in range(5)]
        # for i, btn in enumerate(btns):
        #     for j in range(10):
        #         grid.addWidget(btn, i, j)
        # self.show()

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')
        # 编辑栏
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        # grid.addWidget(author, 2, 0)
        # grid.addWidget(authorEdit, 2, 1)
        #
        # grid.addWidget(review, 3, 0)
        # grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())
