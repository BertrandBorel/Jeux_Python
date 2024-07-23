from random import randint

class lancer_des :
    def __init__(self, de):
        pass

    # Méthode pour lancer 1 seul dé
    def lancer(self):
        de = randint(1, 6)
        print(f"-------------------------------------\n Résultat de votre dé : {de}")
        return de 
        
    # Méthode pour lancer 2 dés
    def lancer_2(self):
        de1 = randint(1, 6)
        de2 = randint(1, 6)
            # On affiche le résultat des dés
        print(f"-------------------------------------\nVotre premier dé : {de1}")
        print(f"Votre deuxième dé : {de2}")
            # On fait le calcul de la somme totale
        somme = de1 + de2 
        print(f"Somme totale du lancer : {somme}")
            # On retourne la valeur pour la stocker ?
        return somme 
         

# Test : 
lanceur = LancerDes()
lanceur.lancer_2()
lanceur.lancer()


