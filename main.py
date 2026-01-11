import time
import threading
from datetime import datetime, timedelta
from pynput import keyboard
import print_heure
import start_menu
from playsound import playsound

new_alarm_val = None
is_typing = False

def alarm_input_worker():
    global new_alarm_val, is_typing
    is_typing = True
    print("\n\n--- ALARM SETTINGS ---")
    new_alarm_val = print_heure.choose_hour()
    is_typing = False

def main(hour_alarme, hour_start):
    global new_alarm_val, is_typing
    
    current_alarme = hour_alarme
    now = datetime.now()
    start_dt = now.replace(hour=hour_start[0], minute=hour_start[1], second=hour_start[2], microsecond=0)
    launch_moment = datetime.now()

    def on_press(key):
        global is_typing
        try:
            if key.char == 'q':
                return False
            if key.char == 'a' and not is_typing:
                t = threading.Thread(target=alarm_input_worker, daemon=True)
                t.start()
        except AttributeError:
            pass

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    while listener.running:
        elapsed = datetime.now() - launch_moment
        current_time_dt = start_dt + elapsed
        
        h, m, s = current_time_dt.hour, current_time_dt.minute, current_time_dt.second
        current_tuple = (h, m, s)

        if new_alarm_val is not None:
            current_alarme = new_alarm_val
            new_alarm_val = None

        if not is_typing:
            print_heure.print_hour(current_tuple)

        if current_alarme is not None and current_tuple == current_alarme:
            print("\n!!! BIP BIP BIP !!!")
            playsound(r"D:\plateforme\clock\reveil.mp3", block=False)
            current_alarme = None

        time.sleep(0.1)

    print("\nSTOP PROGRAM")
    

def start_program():
    alarm = start_menu.alarm_menu()
    start = start_menu.start_menu()
    main(alarm, start)

if __name__ == "__main__":
    start_program()