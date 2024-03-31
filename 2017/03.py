import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

T=int(L)
number=1
l,r,u,d=0,0,0,0
row,col=0,0
D={1:(0,0)}
while number<T:
    r+=1
    while col<r:
        col+=1
        number+=1
        D[number]=(row,col)
    u-=1
    while row>u:
        row-=1
        number+=1
        D[number]=(row,col)
    l-=1
    while col>l:
        col-=1
        number+=1
        D[number]=(row,col)
    d+=1
    while row<d:
        row+=1
        number+=1
        D[number]=(row,col)
print(abs(D[T][0])+abs(D[T][1]))

T=int(L)
l,r,u,d=0,0,0,0
row,col=0,0
D={(0,0):1}

def f(r,c):
    res=0
    for dr,dc in [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]:
        t=(r+dr,c+dc)
        if t in D:
            res+=D[t]
    if res>T:
        print(res)
        exit()
    return res

while True:
    r+=1
    while col<r:
        col+=1
        D[(row,col)]=f(row,col)
    u-=1
    while row>u:
        row-=1
        D[(row,col)]=f(row,col)
    l-=1
    while col>l:
        col-=1
        D[(row,col)]=f(row,col)
    d+=1
    while row<d:
        row+=1
        D[(row,col)]=f(row,col)
