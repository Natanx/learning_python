#il s'agit de trouver la période d'un pendule simple a partir de n'importre quelle longueur de pendule donnée par l'utilisateur.
# Rappelons la formule de période d'un pendule simple : 2pi x Racine carré de la longueur du pendule sur la constante gravitationelle

from math import *

L = input("Quel est la longueur de votre pendule ? ")
L = float(L)
g = 9.8
S = 2*pi*sqrt(L/g)

print("La période de votre pendule est de : ",S,".")
