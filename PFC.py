#DEBUT

# Definir la fonction PFC
     # Si PFC a pour valeur 1
        # Alors retourner "pierre"
    # Sinon si PFC a pour valeur 2
        # Alors retourner "feuille"
    # Sinon si PFC a pour valeur 3
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

# Initialisation de PFCbot
# On admet que la fonction randomPFC existe et renvoie (1, 2, 3) de façon aléatoire
# Utiliser la fonction randomPFC
# retourner la fonction PFC

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










# instruction pfc
# pas de code
# a envoyer sur github en public avec nom et prénom
# pseudo code
# 2 éléments a dev inconnue
# on admet que la fct random existe et renvoie un para(p/f/c) aléatoire
# de même pour l'input
# pas d'autre chose def par python


