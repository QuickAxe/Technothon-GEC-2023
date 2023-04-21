import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from news import getNews


class News(QWidget):
    _TotalNews = 3
    _MaxSize = 60

    def __init__(self, ax: int, ay: int, aw: int, ah: int, fontsize: int):
        self.fontsize = fontsize
        super().__init__()
        self.News = getNews()
        self.setWindowTitle("News")
        # setting geometry of main window
        # self.setGeometry(ax, ay, aw, ah)

        # creating a vertical layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setSizeConstraint(int(aw * 1 / 4))
        self.newsLabels = self.createNewsLabels()
        # creating font object
        # seperator = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        for label in self.newsLabels:
            self.layout.addWidget(label)
            # self.layout.addSpacerItem(seperator)
            # self.layout.addWidget(seperator)
        # setting the layout to main window
        self.setLayout(self.layout)

    def getNewsJson(self):
        return self.News

    def createNewsLabels(self):
        i = 0
        labels = []
        font = QFont("Arial", self.fontsize, QFont.Bold)
        for article in self.News["articles"][: self._TotalNews]:
            label = QLabel()
            label.setAlignment(Qt.AlignCenter)
            label.setFont(font)
            label.setStyleSheet("border: 1px solid white;    border-radius: 5px")
            text = article["title"]
            text = (
                text if len(text) < self._MaxSize else text[: self._MaxSize - 3] + "..."
            )
            label.setText(text)
            labels.append(label)
        # sep = QLabel()
        # sep.setAlignment(Qt.AlignCenter)
        # sep.setFont(font)
        # text = '-'*self._MaxSize
        # print(text)
        # sep.setText(text)
        # tween(labels,sep)
        # for label in labels:
        #     print(label)
        return labels


if __name__ == "__main__":
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = News(0, 0, 100, 100, 12)

    # showing all the widgets
    window.show()

    # start the app
    App.exit(App.exec_())
