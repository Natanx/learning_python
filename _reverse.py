#il s'agit d'a partir d'un mot donnée en retourner l'inverse, eg : bulgroz > zorglub

a,b = "merghez",""
L = len(a)
s = L-1

while s>=0:
    b+=a[s]
    s-=1

print(b)
