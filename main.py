from datetime import datetime
import time

# Global variables
manual_hour = 0
manual_minute = 0
manual_second = 0
alarm_time = None
alarm_active = False

def display_menu():
    print("\n" + "="*40)
    print("1. Display Clock")
    print("2. Set Time")
    print("3. Set Alarm")
    print("4. Quit")
    print("="*40)

def get_hour_sys():
    now = datetime.now()
    time_tuple = (now.hour, now.minute, now.second)
    return time_tuple

def format_time(h, m, s):
    """Format time as HH:MM:SS"""
    return f"{h:02d}:{m:02d}:{s:02d}"

def increment_time(h, m, s):
    """Increment time by 1 second (like clock.py)"""
    s += 1
    if s >= 60:
        s = 0
        m += 1
        if m >= 60:
            m = 0
            h += 1
            if h >= 24:
                h = 0
    return (h, m, s)

def set_time():
    global manual_hour, manual_minute, manual_second, alarm_time, alarm_active
    
    print("\nSet Manual Time")
    while True:
        try:
            h = int(input("Hour (0-23): "))
            m = int(input("Minute (0-59): "))
            s = int(input("Second (0-59): "))
            
            if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
                # Set manual time using simple variables
                manual_hour = h
                manual_minute = m
                manual_second = s
                print(f"Manual time set to: {format_time(h, m, s)}")
                
                # Display the manual time after setting it
                print("\nDisplaying manual time (Ctrl+C to stop)...")
                try:
                    while True:
                        print(f"\rTime: {format_time(manual_hour, manual_minute, manual_second)}", end='', flush=True)
                        
                        # Check alarm with manual time
                        if alarm_time and alarm_active:
                            if manual_hour == alarm_time[0] and manual_minute == alarm_time[1] and manual_second == alarm_time[2]:
                                print("\n\n" + "="*50)
                                print("Biiiiiiip x)")
                                print(f"Alarm time: {format_time(manual_hour, manual_minute, manual_second)}")
                                print("="*50 + "\n")
                                alarm_active = False
                                alarm_time = None
                        
                        # Increment time by 1 second (like clock.py)
                        manual_hour, manual_minute, manual_second = increment_time(manual_hour, manual_minute, manual_second)
                        
                        time.sleep(1)
                except KeyboardInterrupt:
                    print("\n\nDisplay stopped.")
                
                return
            else : 
                print("ERROR: Invalid value! Please follow the instructions")
                
        except ValueError:
            print("Error: Enter only numbers")

def display_time():
    global alarm_time, alarm_active
    
    # Always display system time
    print("\nDisplaying system time (Ctrl+C to stop)...")
    
    try:
        while True:
            h, m, s = get_hour_sys()
            print(f"\rTime: {format_time(h, m, s)}", end='', flush=True)
            
            # Check alarm with system time
            if alarm_time and alarm_active:
                if h == alarm_time[0] and m == alarm_time[1] and s == alarm_time[2]:
                    print("\n\n" + "="*50)
                    print("Biiiiiiip x)")
                    print(f"Alarm time: {format_time(h, m, s)}")
                    print("="*50 + "\n")
                    alarm_active = False
                    alarm_time = None
            
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nDisplay stopped.")

def set_alarm():
    global alarm_time, alarm_active
    
    print("\nSet Alarm")
    while True:
        try:
            h = int(input("Hour (0-23): "))
            m = int(input("Minute (0-59): "))
            s = int(input("Second (0-59): "))
            
            if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
                alarm_time = (h, m, s)
                alarm_active = True
                print(f"Alarm set for: {format_time(h, m, s)}")
                return
            else : 
                print("ERROR: Invalid value! Please follow the instructions")
                
        except :
            print("Error: Enter only numbers")

def main():
    print("Clock Application Started!")
    
    while True:
        display_menu()
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                display_time()
            elif choice == 2:
                set_time()
            elif choice == 3:
                set_alarm()
            elif choice == 4:
                print("Stopped by user")
                return
            else:
                print("Oops wrong choice!")
        
        except KeyboardInterrupt:
            print("\n\nStopped by user")
            return


if __name__ == "__main__":
    main()
