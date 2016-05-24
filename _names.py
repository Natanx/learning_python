#Il s'agit de trier en deux listes les prénoms contenant dans l'une moins de 6 caractères et dans dans l'autre 6 ou plus à partir
#d'une même liste t1 contenant tout les prenoms.

t1=["Jean","Maximilien","Brigitte","Sonia","Jean-pierre","Sandra","Léa","Anna"]
L,i=len(t1),0
t2,t3=[],[]

while i<L:
    if len(t1[i])<6:
        t2.append(t1[i])
    else:
        t3.append(t1[i])
    i+=1

print("Dans la liste de prénoms : ",t1," ")
print(t2," on moins de 6 lettres et ")
print(t3," possèdent plus de 6 lettres")
