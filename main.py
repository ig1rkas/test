import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt

from random import randint

class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setBrush(QColor(255, 255, 0)) 
        
        diameter = randint(10, 200)
        painter.drawEllipse(randint(10, 200), randint(10, 200), diameter, diameter)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.generatebutton.clicked.connect(self.draw)
        
        
    
    def draw(self):
        self.circle_widget = CircleWidget()
        self.setCentralWidget(self.circle_widget) 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

