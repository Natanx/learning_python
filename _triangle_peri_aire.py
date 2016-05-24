#il s'agit de savoir l'air et le périmètre d'un triangle ou l'utilisateur rentre les trois longueurs du triangles. Rappelons
# la formule du calcul de l'air d'un triangle quelconque : Racine carré de (d x (d-a) x (d-b) x (d-c)) ou a,b et c sont les côté du
#triangle et d le demi périmètre du triangle

from math import *

a, b, c = input("Longeur du premier côté : "),input("Longueur du 2e côté : "),input("Longueur du 3e côté : ")
a, b, c = float(a), float(b), float(c)
d = (a+b+c)/2.0
S = sqrt(d*(d-a)*(d-b)*(d-c))

print("Ce triangle a un périmètre de ",2*d," cm et une aire de ",S," cm².")
