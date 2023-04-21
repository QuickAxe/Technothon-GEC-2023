
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from fitnessTracker import fitData

class Health(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("health")
        self.layout = QHBoxLayout()
        
        self.fitData = fitData()
        
        
        self.healthInfoLayout = QVBoxLayout()
        heartbeat = self.fitData['heartRate']
        sleep = self.fitData    ['sleep']
        Sp02 =  self.fitData    ['SpO2']
        self.stepGoal = self.fitData ['stepGoal']
        
        font = QFont("Arial", 30, QFont.Bold)
        heartLabel = self.createLabel(str(heartbeat)+" bpm",font)
        
        font = QFont("Arial", 10, QFont.Bold)
        sleepLabel = self.createLabel("sleep "+str(sleep),font)
        
        font = QFont("Arial", 15, QFont.Bold)
        sp02Label = self.createLabel("spO2 "+str(Sp02),font)
        
        font = QFont("Arial", 10, QFont.Bold)
        stepLabel = self.createLabel("stepgoal "+str(self.stepGoal),font)
        
        
        self.healthInfoLayout.addWidget(sleepLabel)
        self.healthInfoLayout.addWidget(heartLabel)
        self.healthInfoLayout.addWidget(sp02Label)
        self.healthInfoLayout.addWidget(stepLabel)
        
        self.layout.addLayout(self.healthInfoLayout)
        
        
        imageLabel = self.createImageLabel()
        self.layout.addWidget(imageLabel)
        
        self.setLayout(self.layout)
        
    def getStepGoal(self):
        return self.StepGoal
      
    def createLabel(self, text,font):
        # print(text)
        label = QLabel()
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setWordWrap(True)
        label.setText(text)
        return label    

    def createImageLabel(self):
        label = QLabel()
        image = QPixmap("weatherIcons/heart.jpeg")
        image.setDevicePixelRatio(5)
        label.setPixmap(image)
        label.setScaledContents(True)
        label.resize(image.width(), image.height())
        return label
    

if __name__ == "__main__":
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Health()

    # showing all the widgets
    window.show()

    # start the app
    App.exit(App.exec_())
