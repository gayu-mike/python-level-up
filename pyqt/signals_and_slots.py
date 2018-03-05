import sys

from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QDial, QDialog, QHBoxLayout, QSpinBox


class SpinBox(QSpinBox):
    # signal should register here
    atzero = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.nzero = 0
        # connect signal and slot
        self.valueChanged.connect(self.check_zero)
        self.valueChanged.connect(self.alert)

    # python native function slot
    def check_zero(self):
        """ slot """
        if self.value() == 0:
            self.nzero += 1
            self.atzero.emit(self.nzero)

    # decorator slot
    @pyqtSlot(int)
    def alert(self, val):
        print('value: {}'.format(val))


class Form(QDialog):
    def __init__(self):
        super().__init__()
        widgets = self.set_widget()
        self.set_layout(*widgets)
        self.bind_action()

    def set_widget(self):
        self.dial = QDial()
        self.spinbox = SpinBox()
        return self.dial, self.spinbox

    def set_layout(self, *widgets):
        layout = QHBoxLayout()
        for w in widgets:
            layout.addWidget(w)
        self.setLayout(layout)

    def bind_action(self):
        # predefined signal and predefined slot
        self.dial.valueChanged.connect(self.spinbox.setValue)
        self.spinbox.valueChanged.connect(self.dial.setValue)
        # user-defined signal and user-defined slot
        self.spinbox.atzero.connect(self.announce)

    @pyqtSlot(int)
    def announce(self, nzero):
        print('nzero: {}'.format(nzero))


def main(cli):
    app = QApplication(cli)
    form = Form()
    form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main(sys.argv)
