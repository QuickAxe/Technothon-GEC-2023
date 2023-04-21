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

app = QApplication(sys.argv)

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
<<<<<<< Updated upstream

        #self.focusedNewsMode(2)
       
=======
        # self.focusedNewsMode(2)
>>>>>>> Stashed changes
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
        self.homeMode()
        
    def homeMode(self):
        self.window = QtWidgets.QWidget()
        self.setCentralWidget(self.window)
        self.HorizontalLayout = QtWidgets.QHBoxLayout()
        self.Layout1 =  QtWidgets.QVBoxLayout()
        news = News(0, 0, 0, 0, 12)
        self.newsJson = news.getNewsJson()
        self.Layout1.addWidget(news)
        weather = Weather()
        self.Layout1.addWidget(weather)
        self.HorizontalLayout.addLayout(self.Layout1)
        self.HorizontalLayout.addWidget(QLabel(), 1)
        
        self.Layout2 =  QtWidgets.QVBoxLayout()
<<<<<<< Updated upstream
        weather = Weather()
        self.Layout2.addWidget(weather,0)
        events = Events(0,0,0,0,12)
        self.Layout2.addWidget(events,0)
        
=======
        health = Health()
        self.Layout2.addWidget(health)
        events = Events(0,0,0,0,12)
        self.Layout2.addWidget(events)
        self.HorizontalLayout.addLayout(self.Layout2)
>>>>>>> Stashed changes
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
    def clownMode(self, n):
        self.window = QtWidgets.QWidget()
        self.setCentralWidget(self.window)
        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(QLabel(), 0,0, 4,1)
        self.focusNews = NewsFocus(self.newsJson,n)
        self.layout.addWidget(self.focusNews, 1,1,2,2)
        self.layout.addWidget(QLabel(), 0,3, 4,1)
        self.window.setLayout(self.layout)
        


if __name__ == "__main__":
# def init():
    window = Window()
    sys.exit(app.exec())

#init()