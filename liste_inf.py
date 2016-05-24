enter = str
t1 = []

while enter != "" :
    enter = input("Veuillez entrer une valeur : ")
    if enter != "" :
        enter = int(enter)
        t1.append(enter)

print (t1)
