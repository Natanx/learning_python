#Demander à l'utilisateur qu'il entre un nombre. Afficher ensuite : soit la racine carrée de ce nombre,
#soit un message indiquant que la racine carrée de ce nombre ne peut être calculée.

from math import *
n = float(input("Donné un nombre quelconque pour en obtenir sa racine. \n"))

if n >= 0:
    print("La racine carré de ",n,"est ",sqrt(n))
else:
    print('La racine carré de ce nombre ne peut être calculé(erreur math)')
