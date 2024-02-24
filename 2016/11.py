import itertools

import sys
from collections import *
from copy import deepcopy

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

def valid(F):
    for i in range(len(F)):
        if F[i][0]!=F[i][1]:
            if any(f[1]==F[i][0] for f in F):
                return False
    return True

def generate_key(E,F):
    return str(E)+','.join(str(f[0])+str(f[1]) for f in sorted(F))

def valid_moves(E,F,next):
    if E+next<0 or E+next>=4:
        return []
    res=[]
    floor=[]
    for i in range(len(F)):
        if F[i][0]==E:
            floor.append((i,0))
        if F[i][1]==E:
            floor.append((i,1))
    for c in itertools.combinations(floor,2):
        copy=deepcopy(F)
        copy[c[0][0]][c[0][1]]+=next
        copy[c[1][0]][c[1][1]]+=next
        if valid(copy):
            res.append(copy)
    for c in floor:
        copy=deepcopy(F)
        copy[c[0]][c[1]]+=next
        if valid(copy):
            res.append(copy)
    return res

def f(A):
    res=0
    Q=deque()
    Q.append((0,A))
    seen=set()
    while Q:
        for _ in range(len(Q)):
            E,F=Q.popleft()
            k=generate_key(E,F)
            if k in seen:
                continue
            seen.add(k)
            if all(x[0]==3 and x[1]==3 for x in F):
                print(res)
                break
            for move in valid_moves(E,F,1):
                Q.append((E+1,move))
            for move in valid_moves(E,F,-1):
                Q.append((E-1,move))
        else:
            res+=1
            continue
        break

f([[0,0],[0,0],[2,1],[1,1],[1,1]])
f([[0,0],[0,0],[2,1],[1,1],[1,1],[0,0],[0,0]])
