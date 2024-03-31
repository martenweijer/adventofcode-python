import sys
from collections import *

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

D=defaultdict(int)

def get(k):
    if k in D:
        return D[k]
    return int(k)

def p1():
    res=0
    i=0
    while i<len(lines):
        line=lines[i]
        if line.startswith('set'):
            _,k,v=line.split()
            D[k]=get(v)
        elif line.startswith('add'):
            _,k,v=line.split()
            D[k]+=get(v)
        elif line.startswith('mul'):
            _,k,v=line.split()
            D[k]*=get(v)
        elif line.startswith('mod'):
            _,k,v=line.split()
            D[k]%=get(v)
        elif line.startswith('jgz'):
            _,k,v=line.split()
            if get(k)>0:
                i+=int(v)
                continue
        elif line.startswith('snd'):
            _,k=line.split()
            res=D[k]
        elif line.startswith('rcv'):
            _,k=line.split()
            if D[k]!=0:
                return res
        i+=1

print(p1())

D1,D2=defaultdict(int),defaultdict(int)

def get(k,D):
    if k in D:
        return D[k]
    return int(k)

res=[0]
i,j=0,0
Q1,Q2=deque(),deque()

def f(i,D,Q1,Q2,count=False):
    while i<len(lines):
        line=lines[i]
        if line.startswith('set'):
            _,k,v=line.split()
            D[k]=get(v,D)
        elif line.startswith('add'):
            _,k,v=line.split()
            D[k]+=get(v,D)
        elif line.startswith('mul'):
            _,k,v=line.split()
            D[k]*=get(v,D)
        elif line.startswith('mod'):
            _,k,v=line.split()
            D[k]%=get(v,D)
        elif line.startswith('jgz'):
            _,k,v=line.split()
            if get(k,D)>0:
                i+=get(v,D)
                continue
        elif line.startswith('snd'):
            _,k=line.split()
            Q1.append(D[k])
            if count:
                res[0]+=1
        elif line.startswith('rcv'):
            _,k=line.split()
            if Q2:
                D[k]=Q2.popleft()
            else:
                return i
        i+=1

D1['p']=0
D2['p']=1

i=f(i,D1,Q1,Q2)
j=f(j,D2,Q2,Q1,True)

while Q1 or Q2:
    i=f(i,D1,Q1,Q2)
    j=f(j,D2,Q2,Q1,True)

print(res[0])
