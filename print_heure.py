import time
import msvcrt
from datetime import datetime
from playsound import playsound


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
    h, m, s = heure
    affichage = f"{h:02d}:{m:02d}:{s:02d}"
    print(f"\r >>> [ {affichage} ] <<< ", end = "", flush=True)

def choose_heure():
    while True:
        try:
            h = int(input("Heure (0-23): "))
            m = int(input("Minute (0-60): "))
            s = int(input("Seconde (0-60): "))
            
            if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
                return (h, m, s)
            else : 
                print("ERREUR : Valeurs impossibles ! Merci de respecter les indications")
                
        except ValueError:
            print("Erreur : Veuillez entrer uniquement des nombres entiers")


def main(hour_start, hour_alarme):
    heure_actuelle = hour_start
    print("\nHorloge lancée. Appuyez sur 'q' pour quitter.")
    
    while True:
        print_heure(heure_actuelle)
        
        if hour_alarme is not None:
            if heure_actuelle == hour_alarme:
                print("\nBIP BIP BIP !")
                playsound(r"D:\plateforme\clock\reveil.mp3", block=False)
        
        heure_actuelle = suivant(heure_actuelle)
        
        if msvcrt.kbhit():
            if msvcrt.getch().decode('utf-8').lower() == 'q':
                print("\nArrêt du programme.")
                break
        time.sleep(1)
        
def start_menu ():
    while True:
        print("\n Bonjour, bonsoir et bienvenue dans l'horloge de mamie, ici vous aurez une horloge en temps réel")
        #time.sleep(5)
        print("\n premièrement vous aurez le choix d'utiliser l'heure actuelle ou de la personnaliser")
        #time.sleep(3)
        print("\n1. Utilisation de l'heure système | 2. Utilisation d'une heure personnalisée")
        choix = input("Votre choix : ")

        if choix == "1":
            return get_hour_sys()
        elif choix == "2":
            print("--- REGLAGE HEURE DEPART ---")
            return choose_heure()
        else : 
            print("ERREUR : Veuillez entrer seulement 1 ou 2")

def alarm_menu ():
    while True:
        print("\n Maintenant vous allez avoir le choix de régler une alarme ou non")
        time.sleep(3)
        activer_alarme = input("Voulez vous régler une horloge ? (o-n): ").lower()

        if activer_alarme == "o":
            print("--- REGLAGE ALARME ---")
            return choose_heure()
        elif activer_alarme == "n":
            alarme = None
            return None
        else :
            print("ERREUR : Répondez par 'o' ou par 'n'.")            

def start_program():
    start = start_menu()
    alarm = alarm_menu()
    
    main(start, alarm)

if __name__ == "__main__":
    start_program()