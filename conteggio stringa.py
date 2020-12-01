

stringa = input("inserisci la stringa... ")
lunghezza = len(stringa)
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
l=0
m=0
n=0
o=0
p=0
q=0
r=0
s=0
t=0
u=0
v=0
z=0
for lettera in stringa:
    if lettera=="a":
        a=a+1
    elif lettera=="b":
        b==b+1
    elif lettera=="c":
        c==c+1
    elif lettera=="d":
        d==d+1
    elif lettera=="e":
        e==e+1
    elif lettera=="f":
        f==f+1
    elif lettera=="b":
        b==b+1
    elif lettera=="h":
        h==h+1
    elif lettera=="i":
        i==i+1
    elif lettera=="l":
        l==l+1
    elif lettera=="m":
        m==m+1
    elif lettera=="n":
        n==n+1
    elif lettera=="o":
        o==o+1
    elif lettera=="p":
        p==p+1
    elif lettera=="q":
        q==q+1
    elif lettera=="r":
        r==r+1
    elif lettera=="s":
        s==s+1
    elif lettera=="t":
        t==t+1
    elif lettera=="u":
        u==u+1
    elif lettera=="v":
        v==v+1
    elif lettera=="z":
        z==z+1

lettere=[a,b,c,d,e,f,g,h,i,l,m,n,o,p,q,r,s,t,u,v,z] 
massimo=lettere[0]
for y in lettere:
    if lettere[y]>massimo:
        massimo=lettere[y]

print("il carattere presnte più volte nella stringa è:" , massimo)

quantità = 0
for x in stringa:
    if x==massimo:
        quantità=quantità+1
print("ed è contenuto", quantità, "volte")

