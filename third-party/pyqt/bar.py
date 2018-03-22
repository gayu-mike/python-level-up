import sys

from PyQt5.QtWidgets import qApp
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMenu

from PyQt5.QtGui import QIcon


def log(*args, **kwargs):
    print(*args, **kwargs)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.menu_bar()
        self.status_bar()
        self.submenu()
        self.show()

    def menu_bar(self):
        """
        QMainWindow.menuBar: menuBar 对象
        QMenu: menu 菜单对象
        QAction: action 功能对象
        addMenu: 添加一个新菜单
        addAction: 添加一个新功能
        """
        menu = self.menuBar()
        menu.setNativeMenuBar(False)  # for mac
        file_menu = menu.addMenu('&文件')
        # 新建
        file_menu.addAction(QAction('新建', self))
        # 导入
        imp_menu = QMenu('导入', self)
        imp_menu.addAction(QAction('本地文件', self))
        imp_menu.addAction(QAction('url', self))
        file_menu.addMenu(imp_menu)
        # 可以直接创建子菜单而不需要QMenu实例
        file_menu.addMenu('没有绑定任何子菜单或者功能的子菜单')
        #TODO: checkbox 勾选栏
        # 退出
        exit = QAction('退出', self)
        exit.setShortcut('Ctrl+Q')
        exit.triggered.connect(qApp.quit)
        file_menu.addAction(exit)

    def status_bar(self):
        statusbar = self.statusBar()
        statusbar.showMessage('statusbar')

    def submenu(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()

    sys.exit(app.exec_())
