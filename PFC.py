#DEBUT
# On admet que la fonction random existe et renvoie (1, 2, 3) de façon aléatoire associer à la variable randomPFC
# Definir la fonction PFC
     # Si randomPFC a pour valeur 1
        # Alors retourner "pierre"
    # Sinon si randomPFC a pour valeur 2
        # Alors retourner "feuille"
    # Sinon si randomPFC a pour valeur 3
        # Alors retourner "ciseaux"
    
#Initialiser le jeu
    #Assigner a la variable ready le retour de l'execution de la fonction input("Etes-vous prêt ? (oui/non) ") 
        #Si ready est egale "oui" 
            #Alors poursuivre l'execution du programme
        #Sinon, arreter le programme

# Initialisation de PFCplayer
 #Assigner a la variable PFCplayer le retour de l'execution de la fonction input("Pierre Feuille ou ciseaux ? ")
        #Si PFCplayer est egale "Pierre"
            #Alors retourner "Pierre"
        #Sinon si PFCplayer est egale "Feuille"
            #Alors retourner "Feuille"
        #Sinon si PFCplayer est egale "Ciseaux"
            #Alors retourner "Ciseaux"
        #Sinon si PFCplayer vaut autre chose
            #Alors renvoyer un message d'erreur 
            #Et proposer de choisir a nouveau

# Definir l'exécution du jeu
# Si PFCplayer rentre une valeur entre 1 et 3 
    # Alors utiliser PFCbot
    # Si PFCplayer vaut "pierre" et que PFCbot vaut "pierre"
        # Alors afficher "égalité"
    # Si PFCplayer vaut "pierre" et que PFCbot vaut "ciseaux"
        # Alors afficher "gagné"
    # Si PFCplayer vaut "pierre" et que PFCbot vaut "feuille"
        # Alors afficher "perdue"
    # Si PFCplayer vaut "feuille" et que PFCbot vaut "feuille"
        # Alors afficher "égalité"
    # Si PFCplayer vaut "feuille" et que PFCbot vaut "pierre"
        # Alors afficher "gagné"
    # Si PFCplayer vaut "feuille" et que PFCbot vaut "ciseaux"
        # Alors afficher "perdue"
    # Si PFCplayer vaut "ciseaux" et que PFCbot vaut "ciseaux"
        # Alors afficher "égalité"
    # Si PFCplayer vaut "ciseaux" et que PFCbot vaut "feuille"
        # Alors afficher "gagné"
    # Si PFCplayer vaut "ciseaux" et que PFCbot vaut "pierre"
        # Alors afficher "perdue"
# Sinon
    # Afficher ("Erreur : choisir une valeur entre 1 et 3 !") 

#Definir une fonction relancer le jeu
    #Demander si le joueur veut continuer
        #Si le joueur veut continuer
            #Alors vider la valeur de PFCplayer
            #Et relancer le programme
        #Sinon arreter le programme    

#FIN

