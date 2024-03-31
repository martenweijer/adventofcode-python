import sys
from collections import *

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

G=defaultdict(list)
for line in lines:
    node,rest=line.split(' <-> ')
    node=node.strip()
    for nei in rest.split(','):
        nei=nei.strip()
        G[node].append(nei)

def dfs(node):
    if node in seen:
        return
    seen.add(node)
    for nei in G[node]:
        dfs(nei)

seen=set()
dfs('0')
print(len(seen))

def dfs(node):
    if node in seen:
        return
    seen.add(node)
    for nei in G[node]:
        dfs(nei)

seen=set()
res=0
for node in G.keys():
    if node not in seen:
        dfs(node)
        res+=1
print(res)
