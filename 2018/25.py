import sys
from collections import *

sys.setrecursionlimit(1500000)

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

index,n=0,len(lines)
arr=[]
while index<n:
    line=lines[index]
    arr.append([int(x) for x in line.split(',')])
    index+=1

G=defaultdict(set)
for i,(w1,x1,y1,z1) in enumerate(arr):
    for j,(w2,x2,y2,z2) in enumerate(arr):
        d=abs(w1-w2)+abs(x1-x2)+abs(y1-y2)+abs(z1-z2)
        if d<=3:
            G[i].add(j)

res=0
seen=set()

def dfs(node):
    if node not in seen:
        seen.add(node)
        for nei in G[node]:
            dfs(nei)

for i in range(len(arr)):
    if i not in seen:
        res+=1
        dfs(i)
print(res)
