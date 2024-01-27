import sys
from collections import *

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
A=[]
for line in lines:
    s=line.split()
    v=int(s[3])
    seconds=int(s[6])
    amount=int(s[13])
    A.append((v,seconds,amount))

for v,seconds,amount in A:
    t,score=0,0
    while t<2503:
        if t+seconds>2503:
            score+=(v*(2503-t))
        else:
            score+=(v*seconds)
        t+=seconds+amount
    res=max(res,score)
print(res)

scores=[]
for i,(v,seconds,amount) in enumerate(A):
    scores.append([])
    t,score=0,0
    while t<2503:
        for j in range(seconds):
            score+=v
            scores[i].append(score)
        for j in range(amount):
            scores[i].append(score)
        t+=seconds+amount

A=defaultdict(int)
for i in range(2503):
    m,key=0,0
    for j in range(len(scores)):
        if scores[j][i]>m:
            m=scores[j][i]
            key=j
    A[key]+=1
print(max(A.values()))
