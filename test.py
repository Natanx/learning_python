t1 = [31,28,31,30,31,30,31,31,30,31,30,31]
t2 = [ ' Janvier ' , ' Février ' , ' Mars ' , ' Avril ' , ' Mai ' , ' Juin ' ,
' Juillet ' , ' Août ' , ' Septembre ' , 'Octobre ' , ' Novembre ' , ' Décembre ' ]
L,c,t3=len(t1)-1,0,[]
​
while c<L:
    t3.append(t2[c])
    t3.append(t1[c])
    c+=1
​
print(t3)
