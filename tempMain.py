from PyQt5 import QtCore, QtGui, QtWidgets
import speech_recognition as sr
import sys

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


def listen(command):
    # command = sr.getCommand().lower()
    if(command == "hello" or command == "hi"):
        sr.speak("hello")
    elif(command == "open weather" or command == "whats the weather" or command == "weather"):
        ###  
        ### !! Add weather info
        ###
        sr.speak("weather")
    elif(command == "news one" or command == "news article one" or command == "expand news article one"):
        ###
        ### !!! news 
        ###
        sr.speak("news[0]")
    elif(command == "news two" or command == "news article two" or command == "expand news article two"):
        ###
        ### !!! news 
        ###
        sr.speak("news[1]")
    elif(command == "news three" or command == "news article three" or command == "expand news article three"):
        ###
        ### !!! news 
        ###
        sr.speak("news[2]")
    elif(command == "health" or command == "health goal" or command == "how many steps today"):
        ###
        ### !!! health, steps today
        sr.speak("your step goal for today is health['stepGoal'] steps")
    elif(command == "mirror mirror on the wall"):
        ####
        #### display clown image here
        ####
       # Window.clownMode()
        sr.speak("I'm the funniest of them all")
    print(command)




def Gui():
    app = QtWidgets.QApplication(sys.argv)

    worker = VoiceWorker()
    thread = QtCore.QThread()
    thread.start()
    worker.moveToThread(thread)

    window = QtWidgets.QWidget()
    window.setGeometry(200, 200, 350, 400)
    window.setWindowTitle("Assistant") 

    title_label = QtWidgets.QLabel(window)
    title_label.setText("Assistant")
    title_label.move(135,10)
    title_label.setFont(QtGui.QFont("SansSerif", 15))

    programs_says = QtWidgets.QLabel(window)
    programs_says.setText("Programs Says")
    programs_says.move(240,100)

    you_says = QtWidgets.QLabel(window)
    you_says.move(25,100)


    you_text = QtWidgets.QLabel(window)
    worker.textChanged.connect(you_text.setText)
    worker.textChanged.connect(listen)
    you_text.move(25,150) 


    start_button = QtWidgets.QPushButton("Start")
    close_button = QtWidgets.QPushButton("Close")


    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addWidget(start_button)
    v_box.addWidget(close_button)
    window.setLayout(v_box)

    start_button.clicked.connect(worker.task)
    #close_button.clicked.connect(QCoreApplication.instance().quit)
    window.show()
    sys.exit(app.exec())


Gui()