#Déterminer si une année (dont le millésime est introduit par l'utilisateur) est bissextile ou non. 
#Une année A est bissextile si A est divisible par 4. Elle ne l'est cependant pas si A est un multiple de 100, 
#à moins que A ne soit multiple de 400.

year = int(input("Entrez l'année s'il vous plaît : "))

if year%4:
    print("Ce n'est pas une année bisextile.")
else:
    print("Année bisextile, oubliez pas le 29 février !")
