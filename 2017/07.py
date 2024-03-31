import sys
from collections import *

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

G=defaultdict(list)
nodes=[]
for line in lines:
    node,_=line.split('(')
    node=node.strip()
    nodes.append(node)
    if '->' in line:
        for nei in line.split('-> ')[1].split(','):
            G[nei.strip()].append(node)
res=None
for node in nodes:
    if len(G[node])==0:
        res=node
print(res)

G=defaultdict(list)
nodes={}
for line in lines:
    node,rest=line.split('(')
    node=node.strip()
    v=int(rest.split(')')[0])
    nodes[node]=v
    if '->' in line:
        for nei in line.split('-> ')[1].split(','):
            G[node].append(nei.strip())

wrong=[None]

def dfs(node):
    res=nodes[node]
    values=[]
    for nei in G[node]:
        v=dfs(nei)
        values.append((nei,v))
        res+=v
    if not wrong[0]:
        arr=[v[1] for v in values]
        C=Counter(arr)
        for k,v in C.items():
            if v==1:
                diff=0
                n=None
                for nei,val in values:
                    if k==val:
                        n=nei
                    else:
                        diff=val-k
                wrong[0]=(n,nodes[n],values,diff,nodes[n]+diff)
    return res

dfs(res)
print(wrong[0])
