import sys
from collections import *

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=[0]
names=set()
G=defaultdict(dict)
for line in lines:
    name,_,cmd,v,_,_,_,_,_,_,dst=line.split()
    dst=dst[:-1]
    G[name][dst]=(cmd,int(v))
    names.add(name)

start='Alice'

def dfs(name,seen,A):
    if len(seen)==len(names):
        score=0
        A.append(start)
        for i in range(1,len(A)):
            src,dst=A[i-1],A[i]
            cmd,v=G[src][dst]
            score+=v if cmd=='gain' else -v
            cmd,v=G[dst][src]
            score+=v if cmd=='gain' else -v
        res[0]=max(res[0],score)
        A.pop()
        return
    for nei,_ in G[name].items():
        if nei not in seen:
            seen.add(nei)
            A.append(nei)
            dfs(nei,seen,A)
            A.pop()
            seen.remove(nei)

dfs(start,{start},[start])
print(res[0])

for name in names:
    G[name]['me']=('x',0)
    G['me'][name]=('x',0)
names.add('me')
res=[0]
dfs(start,{start},[start])
print(res[0])
