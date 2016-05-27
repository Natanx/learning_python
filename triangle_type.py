#Demander à l'utilisateur d'entrer trois longueurs a, b, c. À l'aide de ces trois longueurs, déterminer s'il est possible de
#construire un triangle. Déterminer ensuite si ce triangle est rectangle, isocèle, équilatéral ou quelconque.
#Attention : un triangle rectangle peut être isocèle.

côtés = float(input("Veuillez entrer les trois longueurs de votre triangles (appuyer sur 'Entré' après chaque valeur) :\n")), float(input()), float(input())
petit1, petit2, grand = sorted(côtés)
triangle_possible = petit1 + petit2 > grand

if triangle_possible:
    if ((petit1 == petit2) and grand != petit1) or ((petit1 == grand) and petit1 != petit2) or ((petit2 == grand) and petit2 != petit1):
        if grand**2 == petit1**2 + petit2**2:
            print("Ce triangle est iso-rectangle")
        else:
            print("Ce triangle est isocèle")
    elif petit1 == petit2 | petit1 == grand | petit2 == grand:
        print("Ce triangle est équilatéral")
    else:
        print("Ce triangle est quelconque ...")
else:
    print("Triangle impossible ...")

input()
