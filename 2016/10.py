import math
import sys
from collections import *

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
V=defaultdict(list)
D={}
O={}
T=[17,61]
for line in lines:
    if line.startswith('value'):
        _,v,_,_,_,bot=line.split()
        V[bot].append(int(v))
    else:
        A=line.split()
        src,lo,hi=A[1],A[6],A[11]
        lo_output,hi_output=A[5]=='output',A[10]=='output'
        D[src]=(lo if not lo_output else None,hi if not hi_output else None)
        if lo_output or hi_output:
            O[src]=(lo if lo_output else None,hi if hi_output else None)
res=[]

def f(bot):
    if len(V[bot])!=2:
        return
    a,b=V[bot]
    V[bot].clear()
    lo,hi=min(a,b),max(a,b)
    if [lo,hi]==T:
        print(bot)
    next_lo,next_hi=D[bot]
    if next_lo:
        V[next_lo].append(lo)
        f(next_lo)
    else:
        if bot in O:
            if O[bot][0] in ['0','1','2']:
                res.append(int(lo))
    if next_hi:
        V[next_hi].append(hi)
        f(next_hi)
    else:
        if bot in O:
            if O[bot][1] in ['0','1','2']:
                res.append(int(hi))

bot=None
for k,v in V.items():
    if len(v)==2:
        bot=k
f(bot)
print(math.prod(res))
