import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
N=len(L)
for i in range(N):
    if L[i]==L[(i+1)%N]:
        res+=int(L[i])
print(res)

res=0
T=N//2
for i in range(N):
    next=(i+N+T)%N
    if L[i]==L[next]:
        res+=int(L[i])
print(res)
