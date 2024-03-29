import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import datetime
import iso8601  # For Date and Time
from getCalendarEvents import getUpcomingEvents


class Events(QWidget):
    _TotalEvents = 3
    _MaxSize = 60

    def __init__(self, ax: int, ay: int, aw: int, ah: int, fontsize: int):
        self.fontsize = fontsize
        super().__init__()
        self.Events = getUpcomingEvents(self._TotalEvents)
        self.setWindowTitle("Events")
        # setting geometry of main window
        self.setGeometry(ax, ay, aw, ah)

        # creating a vertical layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setSizeConstraint(ah)
        self.eventsLabels = self.createEventsLabels()
        # creating font object
        # seperator = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        for label in self.eventsLabels:
            self.layout.addWidget(label)
            # self.layout.addSpacerItem(seperator)
            # self.layout.addWidget(seperator)
        # setting the layout to main window
        self.setLayout(self.layout)

    def createEventsLabels(self):
        i = 0
        labels = []
        font = QFont("Arial", self.fontsize, QFont.Bold)
        for event in self.Events:
            label = QLabel()
            label.setAlignment(Qt.AlignCenter)
            label.setFont(font)
            label.setStyleSheet("border: 1px solid white;    border-radius: 5px")
            start = event["start"].get("dateTime", event["start"].get("date"))
            _date_obj = iso8601.parse_date(start)
            if _date_obj.time().hour == 0 and _date_obj.time().minute == 0:
                date_and_time = _date_obj.strftime("%Y-%m-%d")
            else:
                date_and_time = _date_obj.strftime("%Y-%m-%d %H:%M")
                # TODO this doesn't change between TimeZones
            summary = event["summary"]
            summary = (
                summary
                if len(date_and_time) + 1 + len(summary) < self._MaxSize
                else summary[: len(date_and_time) + 1 + self._MaxSize - 3] + "..."
            )
            text = f"{date_and_time} {summary}"
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
    window = Events(0, 0, 100, 100, 12)

    # showing all the widgets
    window.show()

    # start the app
    App.exit(App.exec_())
