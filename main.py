import sys
import random

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

WINDOW_SIZE = (576, 461)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.createCircle(qp)
            qp.end()

    def createCircle(self, qp):
        qp.setBrush(Qt.yellow)
        coords = (random.randrange(10, WINDOW_SIZE[0] - 10 + 1), random.randrange(10, WINDOW_SIZE[
            1] - 10 + 1))
        radius = random.randrange(10, min(WINDOW_SIZE[0] - coords[0] + 1, coords[0] + 1,
                                          WINDOW_SIZE[1] - coords[1] + 1, coords[1] + 1))
        qp.drawEllipse(*coords, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())