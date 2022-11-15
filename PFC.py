#DEBUT
from random import *

#Definir PFCbot
def PFCbot():
    #Cette fonction permet à l'ordinateur de générer aléatoirement un nombre entre 1 et 3
    #n egal une valeur aléatoire entre 1 et 3
    n = randint(1,3)
    #Si n est égal à 1
    if n == 1:
        #Alors PFCbot égal "Pierre"
        PFCbot = "Pierre"
    #Sinon si n égal 2 
    elif n == 2:
        #Alors PFCbot égal "Feuille"
        PFCbot = "Feuille"
    #Sinon si n égal 3
    elif n == 3:
        #Alors PFCbot égal "Ciseaux"
        PFCbot = "Ciseaux"
    return PFCbot

# Definir la fonction PFCplayer
def PFCplayer():
    # Si PFC a pour valeur 1
    if PFCplayer == "Pierre":
        # Alors retourner "Pierre"
        PFCplayer = "Pierre"
    # Sinon si PFC a pour valeur 2
    elif PFCplayer == "Feuille":
        # Alors retourner "Feuille"
        PFCplayer = "Feuille"
    # Sinon si PFC a pour valeur 3
    elif PFCplayer == "Ciseaux":
        # Alors retourner "Ciseaux"
        PFCplayer = "Ciseaux"
    else:
        print("ERREUR, veuillez entrer une valeur correcte (Pierre, Feuille ou Ciseaux")

    
#Initialiser le jeu
#Assigner a la variable ready le retour de l'execution de la fonction input("Etes-vous prêt ? (oui/non) ") 
ready = input("Etes-vous prêt ? (oui/non)")
#Si ready est egale "oui"
if ready == "oui":  
    #Alors poursuivre l'execution du programme
    print("Nouvelle partie ! Choisir, etre Pierre, Feuille et Ciseaux. Ensuite si vous souhaitez arrêter votre partie écrivez : stop")
    while PFCplayer != "stop":
        PFCplayer = input()
        print("Player: ",PFCplayer)
        print(PFCbot())
        # Si PFCplayer vaut "Pierre" et que PFCbot vaut "Pierre"
        if PFCplayer == "Pierre" and PFCbot() == "Pierre" :
             # Alors afficher "égalité"
            print("égalité")
        # Si PFCplayer vaut "Pierre" et que PFCbot vaut "Ciseaux"
        elif  PFCplayer == "Pierre" and PFCbot() == "Ciseaux" :
            # Alors afficher "gagné"
            print("gagné")
        # Si PFCplayer vaut "Pierre" et que PFCbot vaut "Feuille"
        elif  PFCplayer == "Pierre" and PFCbot() == "Feuille":
            # Alors afficher "perdue"
            print("perdue")
        # Si PFCplayer vaut "Feuille" et que PFCbot vaut "Feuille"
        elif  PFCplayer == "Feuille" and PFCbot() == "Feuille":
            # Alors afficher "égalité"
            print("égalité")
        # Si PFCplayer vaut "Feuille" et que PFCbot vaut "Pierre"
        elif  PFCplayer == "Feuille" and PFCbot() == "Pierre":
            # Alors afficher "gagné"
            print("gagné")
        # Si PFCplayer vaut "Feuille" et que PFCbot vaut "Ciseaux"
        elif  PFCplayer == "Feuille" and PFCbot() == "Ciseaux":
            # Alors afficher "perdue"
            print("perdue")
        # Si PFCplayer vaut "Ciseaux" et que PFCbot vaut "Ciseaux"
        elif  PFCplayer == "Ciseaux" and PFCbot() == "Ciseaux":
            # Alors afficher "égalité"
            print("égalité")
        # Si PFCplayer vaut "Ciseaux" et que PFCbot vaut "Feuille"
        elif  PFCplayer == "Ciseaux"and PFCbot() == "Feuille":
            # Alors afficher "gagné"
            print("gagné")
        # Si PFCplayer vaut "Ciseaux" et que PFCbot vaut "Pierre"
        elif  PFCplayer == "Ciseaux" and PFCbot() == "Pierre":
            # Alors afficher "perdue"
            print("perdue")
        # Sinon Afficher ("Erreur : choisir une valeur possible (Pierre, Feuille ou Ciseaux) !") 
        else:
            print("Erreur : choisir une valeur possible (Pierre, Feuille ou Ciseaux) !")
#Sinon, arreter le programme
elif ready == "non":
    print("Fin de la partie")




# #Definir une fonction relancer le jeu
# def restart():
#     #Demander si le joueur veut continuer
#     restart = str(raw_input("Voulez vous continuez ? (oui/non)"))
#     #Si le joueur veut continuer
#     if restart == "oui": 
#         restart_program
#     #Sinon arreter le programme    
#     elif restart == "non": 
#         print("Gameover")
#     else :
#         print("ERREUR , Veuillez écrire oui ou non")

# #FIN
