'''Jeu pierre-feuille-papier-ciseau classique, en 3 manches.'''

import random 

# Message d'accueil
print("Bienvenue dans le jeu shifumi !")


# Fonction du jeu
def partie():
    
    # Points des joueurs
    p_user = 0
    p_ordi = 0
    # sélection d'un élément aléatoire
    liste = ["caillou", "papier", "ciseau"]
    
    print("La partie commence !")

    while p_user < 3 and p_ordi < 3 :

        coup_utilisateur = input("Entrez votre coup : ")
        if coup_utilisateur not in liste :
            print("Entrez une valeur valide : 'caillou', 'papier' ou 'ciseau' ! ")
            coup_utilisateur = input("Entrez votre coup : ")
        else : 
            pass
            # print("Votre coup : ", coup_utilisateur)

        coup_ordi = random.choice(liste)
        print("Coup de l'ordinateur :", coup_ordi)

        calcul = coup_utilisateur + coup_ordi


        if calcul == 'ciseaupapier'or calcul == 'caillouciseau' or calcul == 'papiercaillou':
            p_user += 1
        elif calcul == 'ciseaucaillou' or calcul == 'cailloupapier' or calcul == 'papierciseau':
            p_ordi += 1
        elif coup_utilisateur == coup_ordi:
            print("===>  Egalité !")
        else :
            "Erreur. Veuillez réessayer"

        print("Votre score : ", p_user)
        print("Score de l'ordinateur : ", p_ordi)
        print("-------------------------")

    if p_user == 3 :
        print("Vous avez gagné ! Félicitations !")
    elif p_ordi == 3 :
        print("Vous avez perdu... Retentez votre chance !")


# fonction pour refaire un partie
def rejouer():
    nouvelle_partie = input("Voulez-vous recommencer ? (O/N)")
    if nouvelle_partie == 'O': 
        pass
    elif nouvelle_partie != 'O':
        exit()

# Boucle pour recommencer la partie, si l'utilisateur le décide.
while True :
    partie()
    rejouer()

