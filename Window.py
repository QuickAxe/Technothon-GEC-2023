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

import speech_recognition as sr


class VoiceWorker(QtCore.QObject):
    textChanged = QtCore.pyqtSignal(str)

    @QtCore.pyqtSlot()
    def task(self):
        r = sr.Recognizer()
        m = sr.Microphone()

        while True:
            print("Say somethig!")
            with m as source:
                audio = r.listen(source)
                print("Got it! Now to recognize it...")
                try:
                    value = r.recognize_google(audio)
                    self.textChanged.emit(value)
                    print("You said: ", value)
                except sr.UnknownValueError:
                    print("Oops")






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
        #self.clownMode()
        #self.focusedNewsMode(2)
       
        # self.focusedNewsMode(2)
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
        self.weatherConsition = weather.getWeatherCondition()
        self.Layout1.addWidget(weather)
        self.HorizontalLayout.addLayout(self.Layout1)
        self.HorizontalLayout.addWidget(QLabel(), 1)
        
        self.Layout2 =  QtWidgets.QVBoxLayout()
        health = Health()
        self.stepGoals = health.stepGoal()
        self.Layout2.addWidget(health,0)
        events = Events(0,0,0,0,12)
        self.Layout2.addWidget(events,0)
        self.HorizontalLayout.addLayout(self.Layout2)
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
        return self.newsJson['articles'][n-1]['description']
    
    def createImageLabel(self, path):
        label = QLabel()
        image = QPixmap(path)
        image.setDevicePixelRatio(5)
        label.setPixmap(image)
        label.setScaledContents(True)
        label.resize(image.width(), image.height())
        return label
    def createLabel(self, text,font):
        # print(text)
        label = QLabel()
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setWordWrap(True)
        label.setText(text)
        return label    
    def clownMode(self):
        self.window = QtWidgets.QWidget()
        self.setCentralWidget(self.window)
        self.layout = QtWidgets.QGridLayout()
        font = QFont("Arial", 30, QFont.Bold)
        label = self.createLabel("I'm the funniest of them all",font)
        self.layout.addWidget(label, 0,0, 1,4)
        self.clownImage = self.createImageLabel("clown.png")
        self.layout.addWidget(self.clownImage, 1,1,2,2)
        self.layout.addWidget(QLabel(), 0,3, 4,1)
        self.window.setLayout(self.layout)
   
    def listen(self, command):
        command = command.lower()
        if(command == "hello" or command == "hi"):
            sr.speak("hello")
        elif(command == "open weather" or command == "whats the weather" or command == "weather"):
            ###  
            ### !! Add weather info
            sr.speak("the weather today is ")
            sr.speak(self.weatherCondition)
            ###
            sr.speak("weather")
        elif(command == "news one" or command == "news article one" or command == "expand news article one"):
            desc =self.focusedNewsMode(1)
            sr.speak(desc)
        elif(command == "news two" or command == "news article two" or command == "expand news article two"):
            ###
            ### !!! news 
            desc =self.focusedNewsMode(2)
            sr.speak(desc)
            ###
            
        elif(command == "news three" or command == "news article three" or command == "expand news article three"):
            ###
            ### !!! news 
            desc =self.focusedNewsMode(3)
            sr.speak(desc)
            ###
        elif(command == "health" or command == "health goal" or command == "how many steps today"):
            ###
            ### !!! health, steps today
            
            sr.speak(f"your step goal for today is health")
            sr.speak(self.stepGoals)
            sr.speak("steps")
        elif(command == "mirror mirror on the wall"):
            self.clownMode()
            sr.speak("I'm the funniest of them all")
        elif(command == "home" or command == "back"  ):
            self.homeMode()
        print(command)

   
def init():
    worker = VoiceWorker()
    thread = QtCore.QThread()
    thread.start()
    worker.moveToThread(thread)

    worker.textChanged.connect(Window.listen)

    threadpool = QThreadPool()
    
    threadpool.start(VoiceWorker.task)


    window = Window()
    app.exec()

if __name__ == "__main__":
    
    init()

#init()