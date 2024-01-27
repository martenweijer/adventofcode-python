import sys
from collections import *

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')
grid=[list(line) for line in lines]

S=set()
D=defaultdict(list)
input=None
for line in lines:
    if ' => ' in line:
        src,dst=line.split(' => ')
        D[src].append(dst)
    elif line:
        input=line

for i in range(len(input)):
    c=input[i]
    if c in D:
        for l in D[c]:
            S.add(input[:i]+l+input[i+1:])
for i in range(1,len(input)):
    c=input[i-1:i+1]
    if c in D:
        for l in D[c]:
            S.add(input[:i-1]+l+input[i+1:])
print(len(S))

D={}
for line in lines:
    if ' => ' in line:
        src,dst=line.split(' => ')
        D[dst]=src
res=0
while input!='e':
    for k,v in D.items():
        if k in input:
            input=input.replace(k,v,1)
            res+=1
print(res)
