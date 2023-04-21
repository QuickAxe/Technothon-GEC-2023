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

if __name__ == "__main__":
    from newsWidget import getNews

    app = QApplication(sys.argv)
    news = getNews()
    n =5
    # print(news["articles"][n - 1])
    window = NewsFocus(news, n)
    sys.exit(app.exec())
