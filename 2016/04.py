import sys
from collections import *

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

def f(s,n):
    res=[]
    for c in s:
        v=ord(c)-ord('a')
        v+=(n%26)
        v%=26
        v+=ord('a')
        v=chr(v)
        res.append(v)
    return ''.join(res)

res=0
storage=None
for line in lines:
    s=line.split('[')[0]
    sector=int(s.split('-')[-1])
    abc=line.split('[')[1][:-1]
    C=Counter(s)
    D=defaultdict(set)
    values=set()
    for k,v in C.items():
        if 'a'<=k<='z':
            values.add(v)
            D[v].add(k)
    values=sorted(list(values),reverse=True)
    cur,count=0,0
    B=True
    for c in abc:
        k=values[cur]
        if c not in D[k]:
            B=False
            break
        count+=1
        if count==len(D[k]):
            cur+=1
            count=0
    if B:
        res+=sector
        hash=s.split('-')[:-1]
        A=[f(x,sector) for x in hash]
        if A[0]=='northpole' and A[1]=='object' and A[2]=='storage':
            storage=sector
print(res)
print(storage)
