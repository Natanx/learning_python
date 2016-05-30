#Définissez une fonction compteMots(ph) qui renvoie le nombre de mots contenus dans la phrase ph. On considère comme mots les ensembles de caractères inclus entre des espaces.

def compteMots(ph):
    c = 0
    for i in range(len(ph)):
        if ph[i] == " ":
            c += 1
            continue
        else:
            continue
    print("Il y a", c, "mot(s).")

compteMots(input("Tapez une phrase, on vous dira combien de mots la composent.\n \n"))
input()
