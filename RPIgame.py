from gpiozero import Servo
import random
from time import sleep
servo=Servo(4)
mylist=["noor","hala","zaina","tala","meqdad"]
choice =random.choice(mylist)

while True:
    userchoice=input("enter a word from these :Noor,Hala,Zaina,Tala,Meqdad : ")
    if userchoice.lower()==choice :
        servo.max()
        print("True")
        print("system choice =",choice)
        sleep(2)
        servo.mid()
        sleep(1)
    if userchoice.lower()!=choice:
        servo.min()
        print("False")
        print("system choice =",choice)
        sleep(2)
        servo.mid()
        sleep(1)
