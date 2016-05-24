from math import *

a, b, c = input("Longeur du premier côté : "),input("Longueur du 2e côté : "),input("Longueur du 3e côté : ")
a, b, c = float(a), float(b), float(c)
d = (a+b+c)/2.0
S = sqrt(d*(d-a)*(d-b)*(d-c))

print("Ce triangle a un périmètre de ",2*d," cm et une aire de ",S," cm².")
