from math import pi

def toRads(deger):
    print('\n',int(deger * (pi/180)),"radians\n")

def toDegers(rads):
    print('\n',int(rads * (180/pi)),end = '°\n')

def reload(response):
    global choice
    if response == "Oui":
        quit()
    elif response == "Non":
        print("\nOptions disponible : \n \n 1 : Convertir des degrés en radians. \n 2 : Convertir des radians en degrés. \n q : Quitter. \n ")
        choice = input('Votre choix : ')
        return choice
    else:
        response = input("\nVeuillez entrez \"Oui\" ou \"Non\" : ")
        reload()

print("Options disponible : \n \n 1 : Convertir des degrés en radians. \n 2 : Convertir des radians en degrés. \n q : Quitter. \n ")
choice = input('Votre choix : ',)

while choice not in (1, 2) :
    if choice == '1':
        toRads(float(input("\nEntrez la valeur de l'angle en degré : ")))
    elif choice == '2':
        toDegers(float(input("\nEntrez la valeur de l'angle en radian : ")))
    elif choice == 'q':
        quit()
    else:
        print("\nNous n'avons pas compris.\n")
        print("Options disponible : \n \n 1 : Convertir des degrés en radians. \n 2 : Convertir des radians en degrés. \n q : Quitter. \n ")
        choice = input('Votre choix : ')
        continue

    response = input("\nSouhaitez vous quitter le programme ? (Oui / Non)\n \n")
    reload(response)
