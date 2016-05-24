#L'utilisateur doit entrer des valeur qui seront automatiquement ajouter dans une liste. Le programme se termine uniquement
#si l'utilisateur tape seulement une fois sur 'Enter'
#A la fin du programme affichez la liste

enter = str
t1 = []

while enter != "" :
    enter = input("Veuillez entrer une valeur : ")
    if enter != "" :
        enter = int(enter)
        t1.append(enter)

print (t1)
