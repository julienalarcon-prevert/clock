import time
from datetime import datetime
from playsound import playsound
from pynput import keyboard
import print_heure

def alarm_menu ():
    while True:
        print("\n Hello and welcome in the grandma's clock, here we will have a clock in real time") 
        time.sleep(5)
        print("\n Firstly,you will have the choice of setting an alarm or not.")
        time.sleep(3)
        activer_alarme = input("Do you want to set a clock? (o-n): ").lower()

        if activer_alarme == "o":
            print("--- SET UP ALARME ---")
            return print_heure.choose_hour()
        elif activer_alarme == "n":
            return None
        else :
            print("ERROR : Answer with 'o' or 'n'.")            
def start_menu ():
    while True:
        print("\n Now, you will have the choice of using the current time or customizing it.")
        time.sleep(3)
        print("\n1. Using the system time | 2. Using a custom time")
        choix = input("Your choise : ")

        if choix == "1":
            return print_heure.get_hour_sys()
        elif choix == "2":
            print("--- SET UP HOUR START ---")
            return print_heure.choose_hour()
        else : 
            print("ERROR : Enter only 1 or 2")