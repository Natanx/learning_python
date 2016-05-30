from dessins_tortue import *

taille, couleur, angle, i = float(input('Taille : ')), input('Couleur : '), 0, 0

if couleur == '':
    couleur = 'black'

ht()
pu()
goto(-250, 0)
pd()

while i < 4:
    star5(taille, couleur, angle)
    pu()
    fd(taille+10)
    pd()
    taille += 15
    i += 1

exitonclick()
