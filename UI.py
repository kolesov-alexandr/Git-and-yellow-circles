from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont


class Window(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(576, 461)
        MainWindow.pushButton = QPushButton("Создать", MainWindow)
        MainWindow.pushButton.setGeometry(180, 180, 161, 81)
        font = QFont()
        font.setPointSize(12)
        MainWindow.pushButton.setFont(font)
