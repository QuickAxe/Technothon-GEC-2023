import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, QTime, Qt
 
from news import getNews
import json

class News(QWidget):
    _TotalNews = 3
    
    def __init__(self, ax: int, ay: int, aw: int, ah: int, fontsize: int):
        super().__init__()
        self.News = getNews()
        # setting geometry of main window
        self.setGeometry(ax, ay, aw, ah)
 
        # creating a vertical layout
        layout = QVBoxLayout()
        self.newsLabels = self.createNewsLabels()
        # creating font object
        seperator = QWidget.QSpacerItem(40, 20, QWidget.QSizePolicy.Expanding, QWidget.QSizePolicy.Minimum) 
        for label in self.newsLabels:
            self.layou.addWidget(label)
            self.layout.addWidget(seperator)
         # setting the layout to main window
        self.setLayout(layout)
    def createNewsLabels(self):
        i = 0
        labels = []
        font = QFont('Arial', self.fontsize, QFont.Bold)
        for article in self.News['articles'][:self._TotalNews]:
            label = QLabel()
            label.setAlignment(Qt.AlignCenter)
            label.setFont(font)
            label.setText(article['title'])
            labels.append(label)
        return labels
    
           
            
            
 
if __name__ == "__main__":    
    # create pyqt5 app
    App = QApplication(sys.argv)
    
    # create the instance of our Window
    window = News(0,0,100,100,120)
    
    # showing all the widgets
    window.show()
    
    # start the app
    App.exit(App.exec_())