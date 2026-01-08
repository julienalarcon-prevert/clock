import time
import msvcrt
from datetime import datetime

# --- FONCTIONS OUTILS ---

def get_hour_sys():
    heure_now = datetime.now()
    # On renvoie un tuple
    return (heure_now.hour, heure_now.minute, heure_now.second)

def suivant(heure):
    # 'heure' est un tuple, on l'extrait pour le calcul
    h, m, s = heure
    s += 1
    if s == 60:
        s = 0 
        m += 1
        if m == 60:
            m = 0
            h += 1
            if h == 24:
                h = 0 
    # On renvoie un nouveau tuple
    return (h, m, s)

def print_heure(heure):
    # Sécurité : on s'assure que 'heure' est bien un tuple avant d'accéder aux index
    h, m, s = heure
    t_h = (h // 10, h % 10)
    t_m = (m // 10, m % 10)
    t_s = (s // 10, s % 10)
    print("\r", t_h[0], t_h[1], ":", t_m[0], t_m[1], ":", t_s[0], t_s[1], sep="", end="", flush=True)

def choose_heure():
    while True:
        try:
            h = int(input("Heure (0-23): "))
            m = int(input("Minute (0-59): "))
            s = int(input("Seconde (0-59): "))
            if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
                # On renvoie un tuple
                return (h, m, s)
            else:
                print("ERREUR : Valeurs impossibles !")
        except ValueError:
            print("Erreur : Entrez des nombres entiers.")

# --- FONCTIONS DE GESTION DES MENUS ---

def menu_demarrage():
    while True:
        print("\n1. Utilisation de l'heure système | 2. Utilisation d'une heure personnalisée")
        choix = input("Votre choix : ")
        if choix == "1":
            # On appelle la fonction et on retourne son résultat (un tuple)
            return get_hour_sys()
        elif choix == "2":
            print("--- REGLAGE HEURE DEPART ---")
            # On appelle la fonction et on retourne son résultat (un tuple)
            return choose_heure()
        else:
            print("ERREUR : Veuillez entrer seulement 1 ou 2.")

def menu_alarme():
    while True:
        activer_alarme = input("\nVoulez-vous régler une alarme ? (o/n) : ").lower()
        if activer_alarme == "o":
            print("--- REGLAGE ALARME ---")
            return choose_heure()
        elif activer_alarme == "n":
            return None
        else:
            print("ERREUR : Répondez par 'o' ou 'n'.")

# --- BOUCLE PRINCIPALE ---

def main(hour_start, hour_alarme):
    heure_actuelle = hour_start
    print("\nHorloge lancée. Appuyez sur 'q' pour quitter.")
    
    while True:
        # Ici heure_actuelle doit être un tuple
        print_heure(heure_actuelle)
        
        if hour_alarme is not None and heure_actuelle == hour_alarme:
            print("\nBIP BIP BIP !")
        
        # suivant() reçoit un tuple et renvoie un tuple
        heure_actuelle = suivant(heure_actuelle)
        
        if msvcrt.kbhit():
            if msvcrt.getch().decode('utf-8').lower() == 'q':
                print("\nArrêt du programme.")
                break
        time.sleep(1)

# --- POINT D'ENTRÉE ---

def start_program():
    # ATTENTION : Il faut bien les parenthèses () pour exécuter les fonctions
    # et stocker leurs TUPLES de retour dans les variables.
    heure_depart = menu_demarrage() 
    heure_alarme = menu_alarme()
    
    # On passe les tuples à la fonction main
    main(heure_depart, heure_alarme)

if __name__ == "__main__":
    start_program()