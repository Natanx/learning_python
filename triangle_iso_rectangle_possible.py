#On cherche si il existe un triangle isocèle-rectangle tel que ses 3 côtés sont des entiers naturels (int) ...

from math import *

côté, hypothénuse = int(0), int(0)

while hypothénuse >= 0:                      # Boucle infini qui se coupe que quand j'aurais trouvé la réponse.

    hypothénuse += 1                         # J'incrémente la longueur de l'hypothénuse a chaque itération de boucle.

    if sqrt( (hypothénuse ** 2) / 2) == int: # Je check si la division du carré de l'hypothénuse est égal à un entier naturel >> ce qui voudrais dire que mon triangle est iso-rectangle.
        côté = sqrt( (hypothénuse ** 2) / 2) # J'affecte la valeur du 'if statement' à ma variable côté.
        break                                # Si le 'if statement' est vérrifié la boucle infini s'arrêtte.

    if hypothénuse == 1000000:               # Si l'hypothénuse devient trop importante, ici 1'000'000, la boucle est aussi interrompu.
        print("impossible de faire ce calcul ...")
        break

if côté:
    print("Pour un hypothénuse de", hypothénuse, "les côtés sont de longueur =", côté)

input()

# pour l'instant le scrip me renvoie qu' il est impossible de faire le calcul. Je sais pas si c'est parce que un tel triangle
# n'existe pas ou alors que j'ai merdé le code.
