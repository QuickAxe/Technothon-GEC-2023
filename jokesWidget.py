from pyjokes import get_jokes
from PyQt5.QtWidgets import QApplication
from random import shuffle

from listWidget import ListWidget
import sys
class Jokes(ListWidget):
    def __init__(self, ax: int, ay: int, aw: int, ah: int, fontsize: int):
        jokes = get_jokes('en', 'neutral')
        shuffle(jokes)
        super().__init__(ax, ay, aw, ah, fontsize, "jokes", jokes,3,150)
 
if __name__ == "__main__":    
    # create pyqt5 app
    App = QApplication(sys.argv)
    
    # create the instance of our Window
    window = Jokes(0,0,200,200,12)
    
    # showing all the widgets
    window.show()
    
    # start the app
    App.exit(App.exec_())