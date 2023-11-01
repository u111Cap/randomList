import random

liste = ["Docteur_D","cap","ibucap","BID","jeChangeDeCap","Outsider",]

liste1 = []
liste2 = []

liste = random.sample(liste,len(liste))

liste1 = liste[:int(len(liste)/2)]

liste2 = liste[int(len(liste)/2):]

print(liste1)
print(liste2)