import sys
from collections import *

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

D=defaultdict(int)
for line in lines:
    x,y=int(line.split('@')[1].split(',')[0]),int(line.split('@')[1].split(',')[1].split(':')[0])
    row,col=int(line.split(':')[1].split('x')[0]),int(line.split(':')[1].split('x')[1])
    for r in range(row):
        for c in range(col):
            D[(r+x,c+y)]+=1

res=0
for v in D.values():
    if v>1:
        res+=1
print(res)

seen=set()
D=defaultdict(list)
for line in lines:
    claim=int(line[1:].split()[0])
    seen.add(claim)
    x,y=int(line.split('@')[1].split(',')[0]),int(line.split('@')[1].split(',')[1].split(':')[0])
    row,col=int(line.split(':')[1].split('x')[0]),int(line.split(':')[1].split('x')[1])
    for r in range(row):
        for c in range(col):
            D[(r+x,c+y)].append(claim)

for v in D.values():
    if len(v)>1:
        for k in v:
            seen.discard(k)
for v in seen:
    print(v)
