import random

liste = ["Docteur_D","cap","ibucap","BID","jeChangeDeCap","Outsider",]

# Renvoie une liste de longueur uniques choisis aléatoirement sans remplacement
liste = random.sample(liste,len(liste))

# fonction renvoie la moitie de la liste 
def halfList(liste) :
    return int(len(liste)/2)

#Affichage des listes
print(liste[:halfList(liste)])
print(liste[halfList(liste):])