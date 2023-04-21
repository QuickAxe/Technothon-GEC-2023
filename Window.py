import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from clockWidget import Clock
from newsWidget import News
from eventsWidget import Events
from newsFocus import NewsFocus
from healthWidget import Health
from weatherWidget import Weather

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Mirror")
        # setting geometry
        self.setGeometry(100, 100, 400, 400)

        # calling method
        # self.default_palette = QtGui.QGuiApplication.palette()
        self.setDarkPallete()
        self.UiComponents()
        self.FocusedNewsMode(2)
        # showing all the widgets
        self.show()

    # @QtCore.pyqtSlot()
    def setDarkPallete(self):
        darkpalette = QPalette()
        darkpalette.setColor(QPalette.Window, QColor(0, 0, 0))
        darkpalette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        darkpalette.setColor(QPalette.Base, QColor(0, 0, 0))
        darkpalette.setColor(QPalette.AlternateBase, QColor(0, 0, 0))
        darkpalette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
        darkpalette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        darkpalette.setColor(QPalette.Text, QColor(255, 255, 255))
        darkpalette.setColor(QPalette.Button, QColor(0, 0, 0))
        darkpalette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        darkpalette.setColor(QPalette.BrightText, Qt.red)
        darkpalette.setColor(QPalette.Highlight, QColor(100, 100, 225))
        darkpalette.setColor(QPalette.HighlightedText, Qt.black)
        app.setPalette(darkpalette)

    def UiComponents(self):
        self.window = QtWidgets.QWidget()
        self.layout = QtWidgets.QGridLayout()
        self.setCentralWidget(self.window)
        clock = Clock(0, 0, 20, 10, 12)

        self.layout.addWidget(clock, 0, 0)
        news = News(0, 0, 0, 0, 12)
        self.newsJson = news.getNewsJson()
        self.layout.addWidget(news, 0, 2)
        self.layout.addWidget(QLabel(), 0, 1, 2, 1)
        # _ = self.layout.addWidget(QLabel())
        events = Events(0, 0, 20, 10, 12)
        # # calendar = QWidget.QCalendar()
        clock4 = Clock(0, 0, 20, 10, 12)
        self.layout.addWidget(clock4, 1, 0)
        self.layout.addWidget(events, 1, 2)

        self.window.setLayout(self.layout)
        
    def homeMode(self):
        self.window = QtWidgets.QWidget()
        self.setCentralWidget(self.window)
        self.HorizontalLayout = QtWidgets.QHBoxLayout()
        self.Layout1 =  QtWidgets.QVBoxLayout()
        news = News(0, 0, 0, 0, 12)
        self.newsJson = news.getNewsJson()
        self.Layout1.addWidget(news, 0)
        health = Health(0,0,0,0,12)
        self.Layout1.addWidget(health,1)
        
        self.HorizontalLayout.addWidget(QLabel(), 1)
        
        self.Layout2 =  QtWidgets.QVBoxLayout()
        weather = Weather(0,0,0,12)
        self.Layout2.addWidget(weather,0)
        events = Events(0,0,0,12)
        self.Layout2.addWidget(events,0)
        
        self.window.setLayout(self.HorizontalLayout)
        
    def focusedNewsMode(self, n):
        self.window = QtWidgets.QWidget()
        self.setCentralWidget(self.window)
        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(QLabel(), 0,0, 4,1)
        self.focusNews = NewsFocus(self.newsJson,n)
        self.layout.addWidget(self.focusNews, 1,1,2,2)
        self.layout.addWidget(QLabel(), 0,3, 4,1)
        self.window.setLayout(self.layout)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
