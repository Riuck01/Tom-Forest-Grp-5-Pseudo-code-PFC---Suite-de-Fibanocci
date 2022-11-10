#DEBUT
# def nterms comme le nombre que l'ont rentre
nterms = int(input("Entrez un nombre: "))
 #premier et deuxieme valeurs des nombres d'or
n1 = 0
n2 = 1
 #afficher la suite de finonacci est:
print(" la suite fibonacci est :")
#afficher la valeur n1 et n2 en enlever la derniere virgule 
print(n1,',', n2, end=',')
#pour i repeter de 2 a n fois
for i in range(2, nterms):
  # next égal n1 + n2
  next = n1 + n2
  #afficher next en enlever la derniere virgule
  print(next, end=',')
  #n1 égal n2 , n2 égal next
  n1 = n2
  n2 = next
#FIN