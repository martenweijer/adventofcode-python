import itertools
import math

import sys
from collections import *

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

S=set()
G=defaultdict(defaultdict)
res=math.inf
for line in lines:
    src,_,dst,_,cost=line.split()
    S.add(src)
    S.add(dst)
    G[src][dst]=int(cost)
    G[dst][src]=int(cost)
for path in itertools.permutations(S):
    F=True
    C=0
    src=path[0]
    for i in range(1,len(path)):
        dst=path[i]
        if dst not in G[src]:
            F=False
            break
        C+=G[src][dst]
        src=dst
    if F:
        res=min(res,C)
print(res)

res=-math.inf
for path in itertools.permutations(S):
    F=True
    C=0
    src=path[0]
    for i in range(1,len(path)):
        dst=path[i]
        if dst not in G[src]:
            F=False
            break
        C+=G[src][dst]
        src=dst
    if F:
        res=max(res,C)
print(res)
