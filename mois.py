'''
Définissez une fonction nomMois(n) qui renvoie le nom du n-ième mois de l'année.
Par exemple, l'exécution de l'instruction :
print(nomMois(4)) doit donner le résultat : Avril.
'''

def nomMois(n):
    mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
    print(mois[n-1])

nomMois(int(input('Entre le numéro du mois concerné : ')))
input()
