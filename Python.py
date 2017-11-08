#Python 2.7.10
def fOnly(list):
    return [x for x in list if isinstance(x, float)]

def fNonPrimes(n):
    return list(filter(lambda x: not is_prime_number(x), range(2, n + 1)))

def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
	return False
    return True

def speedLimit():
    while True:
        try:
            speedLimit = int(raw_input("Enter speed limit: "))
            speedGoing = int(raw_input("Enter speed you are going: "))
            if speedLimit < 0 or speedGoing < 0:
                print "Numbers entered cannot be less than 0."
            else:
                if speedGoing > speedLimit:
                    fine = 200
                if speedGoing >= speedLimit + 5:
                    for x in range(speedLimit + 5, min(speedGoing, speedLimit + 20)):
                        fine += 500
                if speedGoing > speedLimit + 20:
                    for x in range(speedLimit + 20, min(speedGoing, speedLimit + 400)):
                        fine += 1000
                if speedGoing > 400:
                    fine = 0
                print("Your speeding fine is: {}".format(fine))
                break;
        except ValueError:
            print("String is not an integer.")

#Question 4 - Tkinter
from Tkinter import *
import tkMessageBox
tkMessageBox.showinfo('This is a title', "Hello World.")

#Question 5
from threading import Thread, Lock
import datetime
import time

mutex = Lock()
theDate = datetime.datetime.now().strftime('%H:%M:%S')

def findTime():
    global theDate
    while True:
        mutex.acquire()
        theDate = datetime.datetime.now().strftime('%H:%M:%S')
        mutex.release()
        time.sleep(0.01)

def displayTime():
    alreadyPrinted = 0
    while True:
        mutex.acquire()
        if alreadyPrinted != theDate:
            print(theDate)
        mutex.release()
        alreadyPrinted = theDate
        time.sleep(0.5)

Thread(target = findTime).daemon = True
Thread(target = displayTime).daemon = True
Thread(target = findTime).start()
Thread(target = displayTime).start()
