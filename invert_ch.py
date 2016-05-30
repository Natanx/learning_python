# Définissez une fonction inverse(ch) qui permette d'inverser les l'ordre des caractères d'une chaîne quelconque. La chaîne inversée sera renvoyée au programme appelant.

def inverse(ch):
    liste = []
    for i in range(len(ch)):
        liste.append(ch[len(ch)-1-i])
        print(end = liste[i])

inverse(input("Entrez ce que vous voulez, on va l'inverser pour vous. "))
input()
