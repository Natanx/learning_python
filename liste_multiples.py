# Écrire un programme qui, étant données deux bornes entières a et b, additionne les nombres multiples de 3 ou 5 compris entre ces bornes. Prendre par exemple a = 0, b = 32 ;
# le résultat devrait donc être : 0 + 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20 + 21 + 24 + 25 + 27 + 30 = 225.

a, b, liste = 0, 32, []

while b > a:
    if (b % 3 == 0) or (b % 5 == 0):
        liste.append(b)
    b -= 1

print(liste)

c = 0

while c < len(liste)-1:
    a = a + liste[c]
    c += 1

print(a)

#je devrais obtenir 225 mais je j'obtiens 222
