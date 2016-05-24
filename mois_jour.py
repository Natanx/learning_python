#Il s'agit à partir de deux listes notés t1 et t2 représentant les mois et leurs nombres de jours respectivement et dans l'ordre
#d'une année civile et a partir de ces deux listes en créer une troisième qui contiendra en alternance le mois suivit du nombres de 
#jour qui le compose.

t1 = [31,28,31,30,31,30,31,31,30,31,30,31]
t2 = [ ' Janvier ' , ' Février ' , ' Mars ' , ' Avril ' , ' Mai ' , ' Juin ' ,
' Juillet ' , ' Août ' , ' Septembre ' , 'Octobre ' , ' Novembre ' , ' Décembre ' ]
L,c,t3=len(t1)-1,0,[]

while c<L:
    t3.append(t2[c])
    t3.append(t1[c])
    c+=1

print(t3)
