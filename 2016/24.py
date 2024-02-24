import itertools
import math

import sys
from collections import *

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

T=0
R,C=len(lines),len(lines[0])
D={}
G={}
for r in range(R):
    for c in range(C):
        if lines[r][c]!='.' and lines[r][c]!='#':
            v=int(lines[r][c])
            T=max(T,v)
            D[v]=(r,c)
for i in range(T+1):
    G[i]={}

def bfs(start,target):
    Q=deque([D[start]])
    seen={D[start]}
    steps=0
    while Q:
        for _ in range(len(Q)):
            r,c=Q.popleft()
            if (r,c)==D[target]:
                G[start][target]=steps
                G[target][start]=steps
                return
            for dr,dc in [[1,0],[0,1],[-1,0],[0,-1]]:
                row,col=r+dr,c+dc
                if 0<=row<R and 0<=col<C and lines[row][col]!='#' and (row,col) not in seen:
                    Q.append((row,col))
                    seen.add((row,col))
        steps+=1

for i in range(T+1):
    for j in range(i+1,T+1):
        bfs(i,j)

def f():
    res=math.inf
    arr=list(range(1,T+1))
    for path in itertools.permutations(arr):
        path=[0]+list(path)
        s=0
        for i in range(1,len(path)):
            src,dst=path[i-1],path[i]
            s+=G[src][dst]
        res=min(res,s)
    return res

print(f())

def f():
    res=math.inf
    arr=list(range(1,T+1))
    for path in itertools.permutations(arr):
        path=[0]+list(path)+[0]
        s=0
        for i in range(1,len(path)):
            src,dst=path[i-1],path[i]
            s+=G[src][dst]
        res=min(res,s)
    return res

print(f())
