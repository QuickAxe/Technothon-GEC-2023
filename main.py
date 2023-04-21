from Window import Window 
import Window
import voiceParser as vs
import sys
import threading 

# import threading

def listen(command):
    # command = vs.getCommand().lower()
    if(command == "hello" or command == "hi"):
        vs.speak("hello")
    elif(command == "open weather" or command == "whats the weather" or command == "weather"):
        ###  
        ### !! Add weather info
        ###
        vs.speak("weather")
    elif(command == "news one" or command == "news article one" or command == "expand news article one"):
        ###
        ### !!! news 
        ###
        vs.speak("news[0]")
    elif(command == "news two" or command == "news article two" or command == "expand news article two"):
        ###
        ### !!! news 
        ###
        vs.speak("news[1]")
    elif(command == "news three" or command == "news article three" or command == "expand news article three"):
        ###
        ### !!! news 
        ###
        vs.speak("news[2]")
    elif(command == "health" or command == "health goal" or command == "how many steps today"):
        ###
        ### !!! health, steps today
        vs.speak("your step goal for today is health['stepGoal'] steps")
    elif(command == "mirror mirror on the wall"):
        ####
        #### display clown image here
        ####
       # Window.clownMode()
        vs.speak("I'm the funniest of them all")
    print(command)


if __name__ == "__main__":
    
    # t1 = threading.Thread(Window.init())
    # t2 = threading.Thread(listen())

    # t1.start()
    # t2.start()

    # t2.join()
    # t1.join()

    listen()