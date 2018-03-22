import sys

from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication


def main(cli):
    app = QApplication(cli)

    def read_all(resp):
        text = resp.readAll().data().decode()
        print(text)
        return text

    req = QNetworkRequest(QUrl('https://httpbin.org/ip'))
    client = QNetworkAccessManager()
    client.finished.connect(read_all)
    resp = client.get(req)
    print(resp)
    app.exec_()
    app.quit.emit()


if __name__ == '__main__':
    main(sys.argv)
