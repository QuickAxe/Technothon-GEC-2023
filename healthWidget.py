import sys
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QApplication, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class NewsFocus(QWidget):
    def __init__(self, ax: int, ay: int, aw: int, ah: int, fontsize: int):
        self.fontsize = fontsize
        super().__init__()
