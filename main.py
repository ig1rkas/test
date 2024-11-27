import sys
import io
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

        painter.setBrush(
            QColor(randint(0, 255), randint(0, 255), randint(0, 255)))

        diameter = randint(10, 200)
        painter.drawEllipse(randint(10, 200), randint(
            10, 200), diameter, diameter)


class UI_text():
    def __init__(self) -> None:
        self.ui = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="generatebutton">
    <property name="geometry">
     <rect>
      <x>74</x>
      <y>312</y>
      <width>261</width>
      <height>121</height>
     </rect>
    </property>
    <property name="text">
     <string>generate button</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>22</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(UI_text().ui)
        uic.loadUi(f, self)
        self.generatebutton.clicked.connect(self.draw)

    def draw(self):
        self.circle_widget = CircleWidget()
        self.setCentralWidget(self.circle_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
