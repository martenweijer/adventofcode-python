import heapq

import sys
from collections import *

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

index,n=0,len(lines)
G=defaultdict(set)
G2=defaultdict(set)
while index<n:
    line=lines[index]
    src,dst=line.split()[1],line.split()[-3]
    G2[src].add(dst)
    G[dst].add(src)
    index+=1

Q=[]
for k,v in G2.items():
    if len(G[k])==0:
        heapq.heappush(Q,k)

res=''
while Q:
    node=heapq.heappop(Q)
    res+=node
    for nei in G2[node]:
        G[nei].remove(node)
        if len(G[nei])==0:
            heapq.heappush(Q,nei)
print(res)

index,n=0,len(lines)
G=defaultdict(set)
G2=defaultdict(set)
while index<n:
    line=lines[index]
    src,dst=line.split()[1],line.split()[-3]
    G2[src].add(dst)
    G[dst].add(src)
    index+=1

Q=[]
for k,v in G2.items():
    if len(G[k])==0:
        heapq.heappush(Q,(0,k))

def f(node):
    return 60+(ord(node)-ord('A')+1)

res=0
wait=[]
while Q or wait:
    while wait:
        heapq.heappush(Q,heapq.heappop(wait))
    while len(wait)<5 and Q:
        time,node=heapq.heappop(Q)
        time+=f(node)
        res=max(res,time)
        for nei in G2[node]:
            G[nei].remove(node)
            if len(G[nei])==0:
                heapq.heappush(wait,(time,nei))
print(res)
