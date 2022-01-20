def bubble_sort(arr):
    sort_req = True
    while sort_req:
        sort_req = False
        for i in range(len(arr)-1):
            if arr[i+1] < arr[i]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sort_req = True
    return arr

#
# random_list_of_nums = [5, 2, 1, 8, 4, 3, 10, 12, 29]
# bubble_sort(random_list_of_nums)
# print(random_list_of_nums)

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen, QPainterPath, QColor, QPolygon
from PyQt5.QtCore import Qt, QTimer, QTimeLine, QLineF, QPoint
import math
import sys
from random import randint

class Window(QMainWindow):

    def __init__(self):

        super().__init__()

        self.title = "PyQt5 Drawing Tutorial"
        self.top = 150
        self.left = 150
        self.width = 1000
        self.height = 1000
        self.dot_num = 3
        self.center = 500
        # self.dots = []
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

    def drawLines(self, qp):
        self.draw_triangle(qp)

    def draw_triangle(self, qp):
        for i in range(self.dot_num):
            color = QColor(randint(0, 250), randint(0, 250), randint(0, 250))
            pen = QPen(color, 1, Qt.SolidLine)
            qp.setPen(pen)
            qp.setBrush(QBrush(color))

            pt_x = math.cos(2 * math.pi * i/self.dot_num) * self.center + self.center
            pt_y = math.sin(2 * math.pi * i/self.dot_num) * self.center + self.center

            next_pt_x = math.cos(2 * math.pi * (i+1)/self.dot_num) * self.center + self.center
            next_pt_y = math.sin(2 * math.pi * (i+1)/self.dot_num) * self.center + self.center

            points = QPolygon([
                QPoint(pt_x, pt_y),
                QPoint(self.center, self.center),
                QPoint(next_pt_x, next_pt_y)
            ])

            qp.drawPolygon(points)




App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())