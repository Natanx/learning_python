from math import *

L = input("Quel est la longueur de votre pendule ? ")
L = float(L)
g = 9.8
S = 2*pi*sqrt(L/g)

print("La période de votre pendule est de : ",S,".")
