import sys
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QApplication, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class NewsFocus(QWidget):
    def __init__(self, news, n):
        super().__init__()
        # self.layout = QtWidgets.QBoxLayout()
        Article = news["articles"][n - 1]
        (Source, Author, Title, Description, Content) = (
            Article["source"],
            Article["author"],
            Article["title"],
            Article["description"],
            Article["content"],
        )
        

        self.setWindowTitle("FocusedNews")

        self.layout = QVBoxLayout()
        font = QFont("Arial", 20, QFont.Bold)
        titleLabel = self.createLabel(Title, Qt.AlignmentFlag.AlignCenter, font)
        font = QFont("Arial", 16, italic=True)
        descLabel = self.createLabel(Description, Qt.AlignmentFlag.AlignCenter, font)
        font = QFont("Arial", 10)
        authorLabel = self.createLabel(Author, Qt.AlignmentFlag.AlignRight, font)
        self.layout.addWidget(titleLabel)
        self.layout.addWidget(descLabel)
        
        self.layout.addWidget(authorLabel)
        self.setLayout(self.layout)
        self.show()

    def createLabel(self, text, alignment, font):
        label = QLabel()
        label.setFont(font)
        label.setAlignment(alignment)
        label.setWordWrap(True)
        label.setText(text)
        return label
    #     self.centralwidget = QtWidgets.QWidget(MainWindow)
    #     self.centralwidget.setObjectName("centralwidget")
    #     self.Title = QtWidgets.QLabel(self.centralwidget)
    #     self.Title.setGeometry(QtCore.QRect(120, 40, 571, 31))
    #     self.Title.setAlignment(QtCore.Qt.AlignCenter)
    #     self.Title.setObjectName("Title")
    #     self.Description = QtWidgets.QLabel(self.centralwidget)
    #     self.Description.setGeometry(QtCore.QRect(120, 90, 571, 20))
    #     self.Description.setAlignment(QtCore.Qt.AlignCenter)
    #     self.Description.setObjectName("Description")
    #     self.Content = QtWidgets.QLabel(self.centralwidget)
    #     self.Content.setGeometry(QtCore.QRect(120, 170, 571, 361))
    #     self.Content.setAlignment(QtCore.Qt.AlignCenter)
    #     self.Content.setObjectName("Content")
    #     self.Date = QtWidgets.QLabel(self.centralwidget)
    #     self.Date.setGeometry(QtCore.QRect(30, 120, 71, 18))
    #     self.Date.setObjectName("Date")
    #     self.Source = QtWidgets.QLabel(self.centralwidget)
    #     self.Source.setGeometry(QtCore.QRect(710, 110, 71, 18))
    #     self.Source.setObjectName("Source")
    #     MainWindow.setCentralWidget(self.centralwidget)
    #     self.retranslateUi(MainWindow)
    #     QtCore.QMetaObject.connectSlotsByName(MainWindow)
    # def retranslateUi(self, MainWindow):
    #     _translate = QtCore.QCoreApplication.translate
    #     MainWindow.setWindowTitle(_translate("MainWindow", "FocusedNews"))
    #     self.Title.setText(_translate("MainWindow", "Title"))
    #     self.Description.setText(_translate("MainWindow", "Description"))
    #     self.Content.setText(_translate("MainWindow", "content"))
    #     self.Date.setText(_translate("MainWindow", "Date"))
    #     self.Source.setText(_translate("MainWindow", "Source"))


if __name__ == "__main__":
    from newsWidget import getNews

    app = QApplication(sys.argv)
    news = getNews()
    n =5
    # print(news["articles"][n - 1])
    window = NewsFocus(news, n)
    sys.exit(app.exec())
