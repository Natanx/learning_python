#En partant de l'exercice précédent, écrivez un script qui détermine si une chaîne de caractères donnée est un palindrome
#(c'est-à-dire une chaîne qui peut se lire indifféremment dans les deux sens), comme par exemple « radar » ou « s.o.s ».

a,b = "anna",""
L = len(a)
s = L-1

while s>=0:
    b+=a[s]
    s-=1

if b==a:
    print(a," est un palindrome")
