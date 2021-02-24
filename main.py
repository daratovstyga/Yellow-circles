import random
import sys
from random import randrange

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import QWidget, QApplication
from UI import Ui_Form


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.f = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.f = True
        self.repaint()

    def new_circle(self, qp):
        r = randrange(2, 400, 2)
        x, y = random.randint(r, self.width() - r), random.randint(r, self.height() - r)
        qp.drawEllipse(QPoint(x, y), r, r)

    def paintEvent(self, event):
        if self.f:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))
            self.new_circle(qp)
            qp.end()
            self.f = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
