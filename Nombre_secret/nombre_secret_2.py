''' Jeu : deviner un nombre avec Python
Source : revue Coding, n°19, p.104.
Objectif : l'utilisateur doit deviner un nombre. L'utilisateur fixe lui-même 
la fourchette (nombre min et nombre max)
Exemple : entre 1 et 1000
L'utilisateur fixe aussi le nombre d'essai qu'il dispose.'''


# importations
import random
import math

# Choix du nombre minimal
nombre_min = int(input("Entrez un nombre minimal : "))

# Choix du nombre maximal
nombre_max = int(input("Entrez un nombre maximal : "))

# Choix du nombre d'essai
nombre_essai = int(input("Choisissez le nombre d'essai que vous voulez pour la partie : "))
print("Vous avez droit à : ", nombre_essai, "essai(s).")

# Génération d'un nombre aléatoire (avec random)
nombre = random.randint(nombre_min, nombre_max)

while nombre_essai != 0 :
    essai = int(input("Entrez un nombre : "))
    if essai == nombre :
        print("Bravo ! Vous avez gagné !")
        break 
    elif essai < nombre :
        print("Le nombre secret est plus grand...")
    elif essai > nombre :
        print("Le nombre secret est plus petit...")
    nombre_essai -= 1

if nombre_essai == 0 :
    print("Vous avez perdu ! Le nombre secret était", nombre, "! Retentez votre chance !")
