import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, QTime, Qt
 
from news import getNews
import json

class News(QWidget):
    _TotalNews = 3
    _MaxSize = 20
    def __init__(self, ax: int, ay: int, aw: int, ah: int, fontsize: int):
        self.fontsize = fontsize 
        super().__init__()
        self.News = getNews()
        # setting geometry of main window
        self.setGeometry(ax, ay, aw, ah)
 
        # creating a vertical layout
        self.layout = QtWidgets.QVBoxLayout()
        self.newsLabels = self.createNewsLabels()
        # creating font object
        # seperator = QWidget.QSpacerItem(40, 20, QWidget.QSizePolicy.Expanding, QWidget.QSizePolicy.Minimum) 
        for label in self.newsLabels:
            self.layout.addWidget(label)
            # self.layout.addWidget(seperator)
         # setting the layout to main window
        self.setLayout(self.layout)
    def createNewsLabels(self):
        i = 0
        labels = []
        font = QFont('Arial', self.fontsize, QFont.Bold)
        for article in self.News['articles'][:self._TotalNews]:
            label = QLabel()
            label.setAlignment(Qt.AlignCenter)
            label.setFont(font)
            text = article['title']
            text = text if text.size < self._MaxSize else text[:_MaxSize-3] + "..."
            label.setText()
            labels.append(label)
        return labels
    
           
            
            
 
if __name__ == "__main__":    
    # create pyqt5 app
    App = QApplication(sys.argv)
    
    # create the instance of our Window
    window = News(0,0,100,100,12)
    
    # showing all the widgets
    window.show()
    
    # start the app
    App.exit(App.exec_())