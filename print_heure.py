import time
from datetime import datetime
from playsound import playsound
from pynput import keyboard

def on_press(key):
    try:
        if key.char == 'q':
            return False
    except AttributeError:
        pass

def get_hour_sys():
    hour_now = datetime.now()
    return (hour_now.hour, hour_now.minute, hour_now.second)

def next(hour):
    h, m , s = hour
    s = s + 1
    if s == 60:
        s = 0 
        m += 1
        if m == 60:
            m = 0
            h += 1
            if h == 24:
                h = 0 
    new_hour = (h, m , s)
    return new_hour

def print_hour(hour):
    h, m, s = hour
    affichage = f"{h:02d}:{m:02d}:{s:02d}"
    print(f"\r >>> [ {affichage} ] <<< ", end = "", flush=True)

def choose_hour():
    while True:
        try:
            h = int(input("hour (0-23): "))
            m = int(input("Minute (0-60): "))
            s = int(input("Seconde (0-60): "))
            
            if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
                return (h, m, s)
            else : 
                print("ERREUR : Value impossible ! please respect the instructions")
                
        except ValueError:
            print("Erreur : Enter only numbers")

def main( hour_alarme,hour_start):
    hour_actuelle = hour_start
    print("\nClock is ready press 'q' for stop the clock.")
    
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    
    while listener.running:
        print_hour(hour_actuelle)
        
        if hour_alarme is not None:
            if hour_actuelle == hour_alarme:
                print("\nBIP BIP BIP !")
                playsound(r"D:\plateforme\clock\reveil.mp3", block=False)
                
                print("Do you want to set up a new alarm ? : (o-n)")
                time.sleep(3)
                choose = input("(o-n)")
                
                if choose == "o" :
                    hour_alarme = choose_hour()
                    print("New alarm set up")
                    print("\nPress 'q' for leave.")
                else : 
                    hour_alarme = None
                    print("Alarme désactivée")
                    print("\nPress 'q' for leave.")
        
        hour_actuelle = next(hour_actuelle)
        time.sleep(1)
    
    print("\nArrêt du programme.")
def alarm_menu ():
    while True:
        print("\n Hello and welcome in the grandma's clock, here we will have a clock in real time") 
        time.sleep(5)
        print("\n Firstly,you will have the choice of setting an alarm or not.")
        time.sleep(3)
        activer_alarme = input("Do you want to set a clock? (o-n): ").lower()

        if activer_alarme == "o":
            print("--- SET UP ALARME ---")
            return choose_hour()
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
            return get_hour_sys()
        elif choix == "2":
            print("--- SET UP HOUR START ---")
            return choose_hour()
        else : 
            print("ERROR : Enter only 1 or 2")


def start_program():
    alarm = alarm_menu()
    start = start_menu()
    
    
    main(alarm,start )

if __name__ == "__main__":
    start_program()