from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush, QPixmap
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 355, 280)
        self.setWindowTitle('Brushes')
        self.show()


    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        qp.drawPixmap(300, 300, QPixmap('icon.png'))
        # self.drawBrushes(qp)
        qp.end()


    def drawBrushes(self, qp):
        pic = QPixmap().load('icon.png')
        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
