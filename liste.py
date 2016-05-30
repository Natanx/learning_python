'''
Définissez une fonction indexMax(liste) qui renvoie l'index de l'élément ayant la valeur la plus élevée dans la liste transmise en argument. Exemple d'utilisation :
serie = [5, 8, 2, 1, 9, 3, 6, 7]
print(indexMax(serie))
4
'''

serie = [5, 8, 2, 1, 9, 3, 6, 7]

def indexMax(liste):
    n = 0
    for i in range(len(liste)):
        if int(liste[i]) > n:
            n = int(liste[i])
    print(n)

indexMax(serie)
input()
