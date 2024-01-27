import math

import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

primes=[int(x) for x in lines]
primes.sort(reverse=True)

def dfs(i,s,A):
    if s>w:
        return
    if s==w:
        res[0]=min(res[0],math.prod(A))
        return
    if i==len(primes):
        return
    else:
        dfs(i+1,s,A)
        dfs(i+1,s+primes[i],A+[primes[i]])

res=[math.inf]
w=sum(primes)//3
dfs(0,0,[])
print(res[0])

res=[math.inf]
w=sum(primes)//4
dfs(0,0,[])
print(res[0])
