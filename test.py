import time
import os
ss=40
mm=40
hh=23

while ss <61:
    time.sleep(1)
    ss+=1
    if ss==60:
        mm+=1
        ss=0
    if mm ==60:
        hh+=1
        mm=0
    if hh==24:
        hh=0
    # os.system('cls' if os.name== 'nt' else 'clear')
    print("\r"f"{hh:02d}:{mm:02d}:{ss:02d}", sep ="", end ="", flush = True)