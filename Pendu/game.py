# Jeu du pendu avec Python

# Source : revue Coding, n°18, p.28-29.


import time
import random

# On demande le nom de l'utilisateur + on affiche un message
name = input("Quel est votre nom ? ")
print("Bonjour " + name, "c'est l'heure de jouer au pendu !")
# temps de latence
time.sleep(1)
# On invite le joueur à saisir une première lettrebob
print("Tapez une lettre pour deviner le mot caché...")
# temps de latence
time.sleep(0.5)

# Liste de mots secrets
words = ['python', 'programmation', 'tresor', 'creativite', 'medium', 'surprise']
# on choisit aléatoirement un des mots
word = random.choice(words)

guesses = ''
turns = 5
while turns > 0 :
    failed = 0 
    for char in word :
        if char in guesses :
            print(char, end="")
        else :
            print("_", end="")  
            failed += 1 

    if failed == 0 :
        print("\nBravo, vous avez gagné !")
        break
    guess = input("\nTapez la lettre de votre choix :")
    guesses += guess 
    if guess not in word :
        turns -= 1
        print("\nHélas, rien !")
        print("\nIl vous reste", + turns, "essais")
        if turns == 0 :
            print("\nPerdu !")