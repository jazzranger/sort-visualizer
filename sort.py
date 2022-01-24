from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import Qt
import colorsys
import math
import sys
from random import randint
import hilbert
from block import Block

class Window(QMainWindow):

    def __init__(self):

        super().__init__()

        self.title = "PyQt5 Drawing Tutorial"
        self.top = 150
        self.left = 150
        self.width = 700
        self.height = 700
        self.block_num = 1000
        self.center = 350
        self._circle_angle = 5760 # углы задаются 1/16-той градуса, полный круг 16*360
        self.block = [Block().get_rgb() for _ in range(self.block_num)]
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def lum (self, r, g, b):
        # Luminosity sorting
        return math.sqrt( .241 * r + .691 * g + .068 * b )

    def step (self, r,g,b, repetitions=1):
        # Step sorting
        lum = math.sqrt( .241 * r + .691 * g + .068 * b )
        h, s, v = colorsys.rgb_to_hsv(r,g,b)
        h2 = int(h * repetitions)
        lum2 = int(lum * repetitions)
        v2 = int(v * repetitions)
        return (h2, lum, v2)

    def drawLines(self, qp):
        # self.block.sort(key=lambda rgb: colorsys.rgb_to_hls(*rgb))
        # self.block.sort(key=lambda rgb: (colorsys.rgb_to_hsv(*rgb)))
        # self.block.sort(key=lambda rgb: self.step(*rgb, 3))
        # self.block.sort(key=lambda rgb: self.lum(*rgb))
        # self.block.sort(key=lambda rgb: hilbert.Hilbert_to_int(rgb))

        self.draw_circles(qp)

    def draw_circles(self, qp):
        for i, block in enumerate(self.block, start=1):
            color = QColor(*block)
            pen = QPen(color, 1, Qt.SolidLine)
            qp.setPen(pen)
            qp.setBrush(QBrush(color))
            span_angle = self._circle_angle/self.block_num
            qp.drawPie(0, 0, self.width, self.height, span_angle*i, span_angle)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())