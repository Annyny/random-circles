import sys
import random

from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton

SIZE_X, SIZE_Y = 1000, 800


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 100, 1000, 800)
        self.setWindowTitle('Случайные окружности')
        self.btn = QPushButton(self)
        self.btn.setStyleSheet('background: rgb(0,255,0);')
        self.btn.setGeometry(SIZE_X // 2 - 90, SIZE_Y // 2 - 15, 200, 30)
        self.btn.setText('Magic')
        self.btn.clicked.connect(self.click)
        self.do_paint = False

    def click(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter(self)
            # Начинаем процесс рисования
            qp.begin(self)
            self.circle(qp)
            # Завершаем рисование
            qp.end()

    def circle(self, qp):
        x = random.randint(100, SIZE_X - 100)
        y = random.randint(100, SIZE_Y - 150)
        d = random.randint(10, 50)
        color = random.choice([Qt.red, Qt.yellow, Qt.blue, Qt.green, Qt.black])
        qp.setPen(QPen(color, 3, Qt.SolidLine))
        qp.drawEllipse(x - d, y - d, 2 * d, 2 * d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())