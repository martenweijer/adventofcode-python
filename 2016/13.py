import sys
from collections import *

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

N=int(L)

def f(x,y):
    v=(x*x)+(3*x)+(2*x*y)+y+(y*y)
    v+=N
    count=0
    while v!=0:
        count+=1
        v&=v-1
    return '#' if count%2==1 else '.'

R,C=50,50
D=[['']*C for _ in range(R)]
for r in range(R):
    for c in range(C):
        D[r][c]=f(c,r)

def f():
    Q=deque([(1,1,[(1,1)])])
    res=0
    seen=set()
    seen.add((1,1))
    T=(39,31)
    while Q:
        for _ in range(len(Q)):
            r,c,A=Q.popleft()
            if (r,c)==T:
                return res
            for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                x,y=r+dx,c+dy
                if 0<=x<R and 0<=y<C and (x,y) not in seen and D[x][y]=='.':
                    seen.add((x,y))
                    Q.append((x,y,A+[(x,y)]))
        res+=1

print(f())

Q=deque([(1,1)])
seen=set()
seen.add((1,1))
for _ in range(50):
    for _ in range(len(Q)):
        r,c=Q.popleft()
        for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            x,y=r+dx,c+dy
            if 0<=x<R and 0<=y<C and (x,y) not in seen and D[x][y]=='.':
                seen.add((x,y))
                Q.append((x,y))
print(len(seen))
