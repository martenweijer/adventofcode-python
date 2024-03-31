import itertools
import math

import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
for line in lines:
    lo,hi=math.inf,-math.inf
    for c in line.split():
        v=int(c)
        lo=min(lo,v)
        hi=max(hi,v)
    res+=hi-lo
print(res)

res=0
for line in lines:
    numbers=[]
    for c in line.split():
        v=int(c)
        numbers.append(v)
    numbers.sort()
    for a,b in itertools.combinations(numbers,2):
        if b%a==0:
            res+=b//a
print(res)
