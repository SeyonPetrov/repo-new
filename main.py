import sys
import random
from UI import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QColor, QPainter


def rand():
    return random.randint(100, 300)


def raan():
    return random.randint(0, 255)


class RandCircle(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(RandCircle, self).__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            pai = QPainter(self)
            pai.begin(self)
            self.painter(pai)
            pai.end()

    def painter(self, pai):
        pai.setBrush(QColor(raan(), raan(), raan()))
        m = rand()
        n = rand()
        pai.drawEllipse(m, n, m // 4, m // 4)
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    rc = RandCircle()
    rc.show()
    sys.exit(app.exec())