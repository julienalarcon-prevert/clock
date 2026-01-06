import time
import msvcrt
from datetime import datetime


def get_hour_sys():
    heure_now = datetime.now()
    return (heure_now.hour, heure_now.minute, heure_now.second)

def suivant(heure):
    h = heure[0]
    m = heure[1]
    s = heure[2]
    s = s + 1
    if s == 60:
        s = 0 
        m += 1
        if m == 60:
            m = 0
            h += 1
            if h == 24:
                h = 0 
    new_heure = (h, m , s)
    return new_heure

def print_heure(heure):
    h = heure[0]
    m = heure[1]
    s = heure[2]
    tuple_h = (h // 10, h % 10)
    tuple_m = (m // 10, m % 10)
    tuple_s = (s // 10, s % 10)
    print("\r", tuple_h[0], tuple_h[1], ":", tuple_m[0], tuple_m[1], ":", tuple_s[0], tuple_s[1], sep="", end="", flush=True)

def choose_heure():
    h = int(input("Heure : "))
    m = int(input("Minute : "))
    s = int(input("Seconde : "))
    return (h, m, s)

def main(hour_start, hour_alarme):
    heure_actuelle = hour_start
    print("\nHorloge lancée. Appuyez sur 'q' pour quitter.")
    
    while True:
        print_heure(heure_actuelle)
        
        if hour_alarme is not None:
            if heure_actuelle == hour_alarme:
                print("\nBIP BIP BIP !")
        
        heure_actuelle = suivant(heure_actuelle)
        
        if msvcrt.kbhit():
            if msvcrt.getch().decode('utf-8').lower() == 'q':
                print("\nArrêt du programme.")
                break
        time.sleep(1)


print("1. Utilisation de l'heure système | 2. Utilisation d'une heure personnalisée")
choix = input("Votre choix : ")

if choix == "1":
    start = get_hour_sys()
else:
    print("--- REGLAGE HEURE DEPART ---")
    start = choose_heure()

print("\nVoulez-vous régler une alarme ? (o/n)")
activer_alarme = input("Votre choix : ").lower()

if activer_alarme == "o":
    print("--- REGLAGE ALARME ---")
    alarme = choose_heure()
else:
    alarme = None

if __name__ == "__main__":
    main(start, alarme)