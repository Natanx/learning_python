t1=[32,5,12,8,3,15,2,75]
L,i=len(t1),0
g=t1[0]

while i<L:
    if g<t1[i]:
        g=t1[i]
    i+=1

print(g)
