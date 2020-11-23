import sys
from random import randrange
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from UI import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.draw_btn.clicked.connect(self.paint)
        self.do_paint = False
        self.coords = (250, 250)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        r = randrange(5, 200)
        self.coords = (randrange(r, self.width() - r), randrange(r, self.width() - r))
        qp.setBrush(QColor(randrange(0, 255), randrange(0, 255), randrange(0, 255)))
        qp.drawEllipse(self.coords[0] - r, self.coords[1] - r, 2 * r, 2 * r)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
