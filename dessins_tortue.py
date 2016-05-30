from turtle import *
from math import *

def carre(taille, couleur, angle):
    "fonction qui dessine un carré de taille, d'angle et de couleur déterminés"
    color(couleur)
    lt(float(angle))
    c = 0
    while c < 4:
        fd(taille)
        lt(90)
        c = c +1

def triangle(taille, couleur, angle):
    "fonction qui dessine un triangle de taille, d'angle et de couleur déterminés"
    color(couleur)
    lt(float(angle))
    c = 0
    while c < 3:
        fd(taille)
        lt(120)
        c += 1

def invert_triangle(taille, couleur, angle):
    "fonction qui dessine un triangle de taille, d'angle et de couleur déterminés"
    color(couleur)
    lt(float(angle))
    c = 0
    while c < 3:
        fd(taille)
        rt(120)
        c += 1


def star5(taille, couleur, angle):
    "fonction qui dessine un triangle de taille, d'angle et de couleur déterminés"
    color(couleur)
    rt(float(angle))
    c = 0
    while c < 5:
        fd(taille)
        lt(144)
        c += 1

def star6(taille, couleur, angle):
    "fonction qui dessine un triangle de taille, d'angle et de couleur déterminés"
    triangle(taille, couleur, angle)
    pu()
    lt(60)
    fd(2/3*taille)
    lt(120)
    fd(1/3*taille)
    lt(180)
    pd()
    invert_triangle(taille, couleur, angle)
    pu()
    fd(1/3*taille)
    rt(120)
    fd(2/3*taille)
    lt(120)
    pd()
