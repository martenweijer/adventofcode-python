import math

import sys
from copy import deepcopy

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
A=[]
for line in lines:
    p=line.split('>, v=')[0][3:].split(',')
    v=line.split('>, v=<')[1].split('>, a=<')[0].split(',')
    a=line.split(', a=<')[1][:-1].split(',')
    A.append(([int(x) for x in p],[int(x) for x in v],[int(x) for x in a]))

lo=math.inf
res=0
copy=deepcopy(A)
for i,(p,v,a) in enumerate(copy):
    for _ in range(1000):
        v[0]+=a[0]
        p[0]+=v[0]
        v[1]+=a[1]
        p[1]+=v[1]
        v[2]+=a[2]
        p[2]+=v[2]
lo,res=math.inf,0
for i,(p,_,_) in enumerate(copy):
    dist=sum(abs(x) for x in p)
    if dist<lo:
        lo=dist
        res=i
print(res)

deleted=set()
for _ in range(100):
    cords={}
    for i,(p,v,a) in enumerate(A):
        if i in deleted:
            continue
        v[0]+=a[0]
        p[0]+=v[0]
        v[1]+=a[1]
        p[1]+=v[1]
        v[2]+=a[2]
        p[2]+=v[2]
        c=(p[0],p[1],p[2])
        if c in cords:
            deleted.add(i)
            deleted.add(cords[c])
        else:
            cords[c]=i
print(len(A)-len(deleted))
