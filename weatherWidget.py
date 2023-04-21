import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from weather import getWeather



class Weather(QWidget):
    def __init__(self, ax: int, ay: int, aw: int, ah: int, fontsize: int):
        self.fontsize = fontsize
        super().__init__()
        self.setWindowTitle("weather")
        self.layout = QHBoxLayout()
        self.weather = getWeather()
        imageLabel = self.createImageLabel()
        self.layout.addWidget(imageLabel)
        
        self.weatherInfoLayout = QVBoxLayout()
        location = self.weather['location']['name']
        temperature = self.weather['current']['temp_c']
        humidity =  self.weather['current']['humidity']
        
        font = QFont("Arial", 20, QFont.Bold)
        locLabel = self.createLabel(location,font)
        font = QFont("Arial", 20, QFont.Bold)
        tempLabel = self.createLabel(str(temperature) + " °C",font)
        font = QFont("Arial", 20, QFont.Bold)
        humLabel = self.createLabel("Humidity"+str(humidity)+"%",font)
        
        self.weatherInfoLayout.addWidget(locLabel)
        self.weatherInfoLayout.addWidget(tempLabel)
        self.weatherInfoLayout.addWidget(humLabel)
        self.layout.addLayout(self.weatherInfoLayout)
        
        
    def createLabel(self, text,font):
        label = QLabel()
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setWordWrap(True)
        label.setText(text)
        return label    

    def createImageLabel(self):
        label = QLabel()
        image = QPixmap("partiallyCloudy.jpg")
        label.setPixmap(image)
        return label


if __name__ == "__main__":
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Weather(0,0,100,100,12,)

    # showing all the widgets
    window.show()

    # start the app
    App.exit(App.exec_())
