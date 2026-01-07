from datetime import datetime
import time

class Clock:
    def __init__(self):
        
        maintenant = datetime.now()
        self.hours = maintenant.hour
        self.minutes = maintenant.minute
        self.seconds = maintenant.second
        self.alarme = None
        self.on_pause = False
    
    def increment_second(self):
        if self.on_pause:
            return
        
        else:
            self.seconds += 1
            if self.seconds >= 60:
                self.seconds = 0
                self.minutes += 1
                if self.minutes >= 60:
                    self.minutes = 0
                    self.hours += 1
                    if self.hours >= 24:
                        self.hours = 0

    def display_time(self, time_tuple=None):
        if time_tuple is not None:
            hours, minutes, seconds = time_tuple

            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds
            print(f"time is {self.time_format()}")
        return self.time_format()
    
    def time_format(self):
        return f"{self.hours:02d} : {self.minutes:02d} : {self.seconds:02d}"
    
    def set_alarme(self,time_tuple):
        hours, minutes, seconds = time_tuple

        self.alarme = hours, minutes, seconds
        print(f"alarme set to {hours:02d} : {minutes:02d} : {seconds:02d}")
        return self.alarme
    
    def check_alarme(self):
        if self.alarme is not None:
            if (self.hours, self.minutes, self.seconds) == self.alarme:
                print("c'est l'heure ! wakeeeee up")
                return True
        return False
    
    def set_pause(self):
        self.on_pause = True
        print("Time paused")

    def ignore_pause(self):
        self.on_pause = False
        print("Here we go again!")

    def start(self):
        try:
            while True:

                if not self.on_pause:
                    print(f"\r{self.time_format()}", end="", flush=True)
                    self.check_alarme

                    time.sleep(1)
                    self.increment_second()
                
                else:
                    time.sleep(0.1)


        except KeyboardInterrupt:
            print("\n stoppe by user")

