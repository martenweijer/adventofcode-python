import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
A=[]
for line in lines:
    _,_,capacity,_,durability,_,flavor,_,texture,_,calories=line.split()
    A.append((int(capacity[:-1]),int(durability[:-1]),int(flavor[:-1]),int(texture[:-1]),int(calories)))

def f(C):
    res=1
    for j in range(4):
        c=0
        for i,ingredient in enumerate(A):
            c+=(ingredient[j]*C[i])
        if c<0:
            return 0
        res*=c
    return res

for i in range(101):
    for j in range(101-i):
        for k in range(101-i-j):
            l=100-i-j-k
            if l>=0:
                value=f([i,j,k,l])
                res=max(res,f([i,j,k,l]))
print(res)

def f(C):
    res=1
    calories=0
    for i,ingredient in enumerate(A):
        calories+=(ingredient[4]*C[i])
    if calories!=500:
        return 0
    for j in range(4):
        c=0
        for i,ingredient in enumerate(A):
            c+=(ingredient[j]*C[i])
        if c<0:
            return 0
        res*=c
    return res

res=0
for i in range(101):
    for j in range(101-i):
        for k in range(101-i-j):
            l=100-i-j-k
            if l>=0:
                value=f([i,j,k,l])
                res=max(res,f([i,j,k,l]))
print(res)
