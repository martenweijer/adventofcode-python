import sys
from collections import *

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

directions=[(0,-1),(-1,0),(0,1),(1,0)]
LEFT,UP,RIGHT,DOWN=0,1,2,3

G=defaultdict(list)
res=[0]
i=0
for line in lines:
    src,dest=line.split('/')
    G[int(src)].append((int(src),int(dest),i))
    G[int(dest)].append((int(dest),int(src),i))
    i+=1

def dfs(node,seen,v):
    res=v
    for x,y,z in G[node]:
        if z in seen:
            continue
        seen.add(z)
        v+=x+y
        res=max(res,dfs(y,seen,v))
        v-=x+y
        seen.remove(z)
    return res

print(dfs(0,set(),0))

res=[0,0]

def dfs(node,seen,v,l):
    if l>res[1]:
        res[0]=v
        res[1]=l
    elif l==res[1]:
        res[0]=max(res[0],v)
    for x,y,z in G[node]:
        if z in seen:
            continue
        seen.add(z)
        v+=x+y
        dfs(y,seen,v,l+1)
        v-=x+y
        seen.remove(z)

dfs(0,set(),0,0)
print(res[0])
