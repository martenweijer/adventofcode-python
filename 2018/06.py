import math

import sys

sys.setrecursionlimit(1500000)

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

directions=[(0,-1),(-1,0),(0,1),(1,0)]
LEFT,UP,RIGHT,DOWN=0,1,2,3

index,n=0,len(lines)
lor,hir=math.inf,-math.inf
loc,hic=math.inf,-math.inf
R,C=0,0
D={}
while index<n:
    line=lines[index]
    x,y=int(line.split(',')[0]),int(line.split(',')[1])
    lor=min(lor,x)
    hir=max(hir,x)
    loc=min(loc,y)
    hic=max(hic,y)
    D[index]=(x,y)
    R+=x
    C+=y
    index+=1

G={}
for row in range(lor,hir+1):
    for col in range(loc,hic+1):
        lo=math.inf
        double=False
        index=None
        for k,v in D.items():
            r,c=v
            distance=abs(row-r)+abs(col-c)
            if distance<lo:
                index=k
                lo=distance
                double=False
            elif distance==lo:
                double=True
        if double:
            G[(row,col)]=-1
        else:
            G[(row,col)]=index
seen=set()
for row in range(lor,hir+1):
    seen.add(G[(row,loc)])
    seen.add(G[(row,hic)])
for col in range(loc,hic+1):
    seen.add(G[(lor,col)])
    seen.add(G[(hir,col)])

def dfs(row,col,seen,i):
    k=(row,col)
    if k in seen or k not in G or G[k]!=i:
        return 0
    seen.add(k)
    res=1
    for dx,dy in directions:
        r=row+dx
        c=col+dy
        res+=dfs(r,c,seen,i)
    return res

res=0
for k,v in D.items():
    if k not in seen:
        value=dfs(v[0],v[1],set(),k)
        res=max(res,value)
print(res)

R//=n
C//=n

def f(row,col):
    distance=0
    for _,v in D.items():
        x,y=v
        distance+=abs(row-x)+abs(col-y)
    return distance<10000

def dfs(row,col,seen):
    k=(row,col)
    if k in seen or not f(row,col):
        return 0
    seen.add(k)
    res=1
    for dx,dy in directions:
        r=row+dx
        c=col+dy
        res+=dfs(r,c,seen)
    return res

print(dfs(R,C,set()))
