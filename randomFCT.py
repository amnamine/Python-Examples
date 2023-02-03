import random

#créer une liste de 10 entiers aléatoires de [0,20]
liste = random.sample(range(10),10)

#afficher la liste
print(liste)

#trier la liste
liste.sort()

#afficher la liste après le tri
print(liste)

#afficher le maximum de la liste
print(max(liste))

#afficher le minimum de la liste
print(min(liste))

#créer une liste de nombres pairs et la trier
pairs = sorted([e for e in liste if e % 2 ==0])

#afficher la liste des nombres pairs triée
print(pairs)