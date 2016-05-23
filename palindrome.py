a,b = "anna",""
L = len(a)
s = L-1

while s>=0:
    b+=a[s]
    s-=1

if b==a:
    print(a," est un palindrome")
