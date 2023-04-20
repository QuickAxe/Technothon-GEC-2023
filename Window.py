import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from clockWidget import Clock
from newsWidget import News
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
 
        # setting title
        self.setWindowTitle("Mirror")
        # setting geometry
        self.setGeometry(100, 100, 800, 800)
 
        # calling method
        # self.default_palette = QtGui.QGuiApplication.palette()
        self.setDarkPallete()
        self.UiComponents()
        # showing all the widgets
        self.show()
    # @QtCore.pyqtSlot()
    def setDarkPallete(self):
        darkpalette = QPalette()
        darkpalette.setColor(QPalette.Window, QColor(0,0,0))
        darkpalette.setColor(QPalette.WindowText, QColor(255,255,255))
        darkpalette.setColor(QPalette.Base, QColor(0,0,0))
        darkpalette.setColor(QPalette.AlternateBase, QColor(0,0,0))
        darkpalette.setColor(QPalette.ToolTipBase, QColor(255,255,255))
        darkpalette.setColor(QPalette.ToolTipText, QColor(255,255,255))
        darkpalette.setColor(QPalette.Text, QColor(255,255,255))
        darkpalette.setColor(QPalette.Button, QColor(0,0,0))
        darkpalette.setColor(QPalette.ButtonText, QColor(255,255,255))
        darkpalette.setColor(QPalette.BrightText, Qt.red)
        darkpalette.setColor(QPalette.Highlight, QColor(100,100,225))
        darkpalette.setColor(QPalette.HighlightedText, Qt.black)
        app.setPalette(darkpalette)
    def UiComponents(self):
        
        self.window = QtWidgets.QWidget()
        self.layout = QtWidgets.QGridLayout()
        self.setCentralWidget(self.window)
        clock = Clock(0,0,200,100,12)
        self.layout.addWidget(clock,0,0)
        news = News(0,0,200,100,12)
        self.layout.addWidget(news,0,1)
        _ = self.layout.addWidget(QLabel(),1,0,1,2)
        # _ = self.layout.addWidget(QLabel())
        clock3 = Clock(0,0,200,100,12)
        self.layout.addWidget(clock3,2,0)
        clock4 = Clock(0,0,200,100,12)
        self.layout.addWidget(clock4,2,1)
        

        self.window.setLayout(self.layout)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec()) 