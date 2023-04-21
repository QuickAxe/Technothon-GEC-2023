import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from weather import getWeather



class Weather(QWidget):
    def __init__(self):
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
        condition = self.weather['current']['condition']['text']
        
        font = QFont("Arial", 10, QFont.Bold)
        condLabel = self.createLabel(condition,font)
        
        font = QFont("Arial", 30, QFont.Bold)
        tempLabel = self.createLabel(str(temperature) + " °C",font)
        
        font = QFont("Arial", 15, QFont.Bold)
        humLabel = self.createLabel("Humidity " +str(humidity)+"%",font)
        
        font = QFont("Arial", 10, QFont.Bold)
        locLabel = self.createLabel(location,font)
        
        
        self.weatherInfoLayout.addWidget(condLabel)
        self.weatherInfoLayout.addWidget(tempLabel)
        self.weatherInfoLayout.addWidget(humLabel)
        self.weatherInfoLayout.addWidget(locLabel)
        
        self.layout.addLayout(self.weatherInfoLayout)
        self.setLayout(self.layout)
        
        
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
        image = QPixmap("partiallyCloudy.jpg",)
        image.setDevicePixelRatio(5)
        label.setPixmap(image)
        label.setScaledContents(True)
        label.resize(image.width(), image.height())

        return label


if __name__ == "__main__":
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Weather()

    # showing all the widgets
    window.show()

    # start the app
    App.exit(App.exec_())
