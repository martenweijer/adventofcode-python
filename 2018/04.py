import sys
from collections import *

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
arr=[]
for line in lines:
    timestamp=line.split(']')[0][1:]
    rest=line.split(']')[1]
    arr.append((timestamp,rest))

arr.sort()
G=defaultdict(int)
guard=0
sleep=False
res=0
time=None
times={}
for t,rest in arr:
    if 'Guard' in rest:
        guard=int(rest.split('Guard #')[1].split()[0])
        if guard not in times:
            times[guard]=defaultdict(int)
        sleep=False
    if 'wakes' in rest:
        i,j=int(time.split(':')[1]),int(t.split(':')[1])
        for x in range(i,j):
            times[guard][x]+=1
        G[guard]+=j-i
        sleep=False
    if 'asleep' in rest:
        sleep=True
        time=t

hi=max(G,key=G.get)
mi=max(times[hi],key=times[hi].get)
print(hi*mi)

hi,mi,id=0,0,0
for k,v in times.items():
    if v:
        a=max(v,key=v.get)
        b=v[a]
        if b>hi:
            hi=b
            mi=a
            id=k
print(id*mi)
