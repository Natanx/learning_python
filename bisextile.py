year = int(input("Entrez l'année s'il vous plaît : "))

if year%4:
    print("Ce n'est pas une année bisextile.")
else:
    print("Année bisextile, oubliez pas le 29 février !")
