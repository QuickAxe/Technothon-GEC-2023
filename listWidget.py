from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
class ListWidget(QWidget):
    _TotalElements = 3
    _MaxSize = 60
    def __init__(self, ax: int, ay: int, aw: int, ah: int, fontsize: int, title, listOfStrings, _TotalElements, _MaxSize):
        self._TotalElements = _TotalElements
        self._MaxSize = _MaxSize    
        self.fontsize = fontsize 
        super().__init__()
        self.List = listOfStrings[:self._TotalElements]
        self.setWindowTitle(title)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setSpacing(0)
        self.Labels = self.createLabels()
        for label in self.Labels:
            self.layout.addWidget(label)
        self.setLayout(self.layout)
    def createLabels(self):
        labels = []
        font = QFont('Arial', self.fontsize, QFont.Bold)
        for element in self.List:
            label = QLabel()
            label.setAlignment(Qt.AlignCenter)
            label.setFont(font)
            label.setStyleSheet("border: 1px solid white;    border-radius: 5px")
            text = element
            text = text if len(text) < self._MaxSize else text[:self._MaxSize-3] + "..."
            label.setText(text)
            labels.append(label)
        
        return labels
    
           
            
            
 
if __name__ == "__main__":    
    # create pyqt5 app
    App = QApplication(sys.argv)
    
    # create the instance of our Window
    window = ListWidget(0,0,100,100,12,"HELP!", ["AAAaaAaAa", "___________", "aAaAaaAaa", "aaAaaA!"],3, 60)
    
    # showing all the widgets
    window.show()
    
    # start the app
    App.exit(App.exec_())