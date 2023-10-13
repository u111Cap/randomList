import random 




nb_eleve = int(input("saisir une taille de  liste paire : "))



while nb_eleve % 2 != 0 or nb_eleve <= 0 :
    nb_eleve =int(input("veuillez svp saisir une taille de liste paire est positive : "))



liste = []

liste1 = []
liste2 = []

for i in range(nb_eleve) :
    element = input(f"rentrer le nom de l'éléve {i+1}: ")
    liste.append(element)

liste1 = random.sample(liste[:int(nb_eleve/2)],int(nb_eleve/2))

liste2 = random.sample(liste[int(nb_eleve/2):],int(nb_eleve/2))
    
print(liste1)
print(liste2)       

