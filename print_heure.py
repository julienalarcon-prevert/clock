import time
from datetime import datetime
from playsound import playsound
from pynput import keyboard
import start_menu

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
    print(f"\r >>> [ {affichage} ] <<< | 'a' : Alarme | 'q' : Quitter ", end="", flush=True)

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