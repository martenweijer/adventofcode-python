import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
for line in lines:
    pass

t=int(L)
dp=[0]*(t//10)
for i in range(1,t//10):
    for j in range(i,t//10,i):
        dp[j]+=i*10
for house in range(1,t//10):
    if dp[house]>=t:
        print(house)
        break

dp=[0]*(t//10)
for i in range(1,t//10):
    v=0
    for _ in range(50):
        v+=i
        if v<t//10:
            dp[v]+=i*11
for house in range(1,t//10):
    if dp[house]>=t:
        print(house)
        break
