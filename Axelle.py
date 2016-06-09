# Programme servant a déterminer si axelle est amoureuse de ninou !!!

i = 0

def amoureuse():
    if input("Es-tu amoureuse de Ninou ? \n \n" ) in ("Oui", "oui", "OUI"):
        print("\nOkay on va tester tout ça !\n \n")
    else:
        print("\nOui ou Non ?\n")
        amoureuse()

def question(num="x", question="Not assigned", no1="/", no2="/", no3="/", solve=0):
    global i
    print("Question", num, ":", question, '\n \n1 -', no1, '\n2 -', no2, '\n3 -', no3)
    if int(input("\n")) == solve:
        i += 1

print("Bonjour Axelle Luxey ! \n \nAujourd'hui on voir si tu aime ton petit amoureux \nen te posant des petites question toutes mims <3")
amoureuse()

question('1', 'Quelle est la couleur préféré de Ninou ?', "Vert", "Bleu", "Rouge", 2)

input()
