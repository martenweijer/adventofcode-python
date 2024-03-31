import sys
from collections import *

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

register=defaultdict(int)
res=0
for line in lines:
    node,op,v,_,key,check,val=line.split()
    v=int(v) if op=='inc' else -(int(v))
    if check=='==':
        if register[key]==int(val):
            register[node]+=v
    elif check=='<':
        if register[key]<int(val):
            register[node]+=v
    elif check=='<=':
        if register[key]<=int(val):
            register[node]+=v
    elif check=='>=':
        if register[key]>=int(val):
            register[node]+=v
    elif check=='>':
        if register[key]>int(val):
            register[node]+=v
    elif check=='!=':
        if register[key]!=int(val):
            register[node]+=v
    res=max(res,max(register.values()))

print(max(register.values()))
print(res)
