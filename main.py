import time
import threading
from datetime import datetime, timedelta
from pynput import keyboard
import print_heure
import start_menu
from playsound import playsound

new_alarm_val = None
new_start_val = None
is_typing = False

def hour_input_worker():
    global new_start_val, is_typing
    is_typing = True
    print("\n\n--- SET UP NEW CURRENT TIME ---")
    new_start_val = print_heure.choose_hour()
    is_typing = False
    print("\nTime updated! Press 'a' for alarm, 'n' for time, 'q' to quit.")

def alarm_input_worker():
    global new_alarm_val, is_typing
    is_typing = True
    print("\n\n--- SET UP NEW ALARM ---")
    new_alarm_val = print_heure.choose_hour()
    is_typing = False
    print("\nAlarm set! Press 'a' for alarm, 'n' for time, 'q' to quit.")

def main(hour_alarme, hour_start):
    global new_alarm_val, new_start_val, is_typing
    
    current_alarme = hour_alarme
    
    now = datetime.now()
    start_dt = now.replace(hour=hour_start[0], minute=hour_start[1], second=hour_start[2], microsecond=0)
    launch_moment = datetime.now()

    def on_press(key):
        global is_typing
        try:
            if key.char == 'q':
                return False
            if not is_typing:
                if key.char == 'a':
                    threading.Thread(target=alarm_input_worker, daemon=True).start()
                if key.char == 'n':
                    threading.Thread(target=hour_input_worker, daemon=True).start()
        except AttributeError:
            pass

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    print("\nClock is running...")

    while listener.running:
        if new_start_val is not None:
            now = datetime.now()
            start_dt = now.replace(hour=new_start_val[0], minute=new_start_val[1], second=new_start_val[2], microsecond=0)
            launch_moment = datetime.now()
            new_start_val = None

        elapsed = datetime.now() - launch_moment
        current_time_dt = start_dt + elapsed
        
        current_tuple = (current_time_dt.hour, current_time_dt.minute, current_time_dt.second)

        if new_alarm_val is not None:
            current_alarme = new_alarm_val
            new_alarm_val = None

        if not is_typing:
            print_heure.print_hour(current_tuple)

        if current_alarme is not None and current_tuple == current_alarme:
            print("\n!!! BIP BIP BIP !!!")
            try:
                playsound(r"D:\plateforme\clock\reveil.mp3", block=False)
            except:
                print("(Sound Error: check your file path)")
            current_alarme = None

        time.sleep(0.1)

    print("\nSTOP PROGRAM")

def start_program():
    alarm = start_menu.alarm_menu()
    start = start_menu.start_menu()
    main(alarm, start)

if __name__ == "__main__":
    start_program()