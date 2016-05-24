#Il s'agit de trier dans deux listes, des nombres issus d'une meme liste. L'une sera composé uniquement de nomber pairs et l'autre
#uniquement de nombres impairs.

t1=[32,5,12,8,3,15,2,75]
L,i=len(t1),0
t2,t3=[],[]

while i<L:
    if t1[i]%2 == 0:
        t2.append(t1[i])
    else:
        t3.append(t1[i])
    i+=1

print("Dans la liste : ",t1," ")
print(t2," sont pairs et ")
print(t3," sont impairs.")
