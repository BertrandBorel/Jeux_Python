'''• Le programme tire un nombre aléatoire
• On demande à l’utilisateur de saisir un nombre
• On lui indique si il est trop petit, trop grand ou s’il a gagné
• Lorsqu’il a gagné on indique à l’utilisateur en combien de fois'''

from random import randint

nombre_secret = randint(0, 100)

nombre_utilisateur = int(input("Veuillez saisir un nombre : "))
tentatives = 0
   

while nombre_utilisateur != nombre_secret :
    if nombre_utilisateur < nombre_secret :
        print("Le nombre secret est plus grand...")
    if nombre_utilisateur > nombre_secret :
        print("Le nombre secret est plus petit...")
    tentatives += 1
    nombre_utilisateur = int(input("Veuillez saisir un nombre : "))

print("Bravo, vous avez trouvé le nombre secret en", tentatives, "tentatives !")
