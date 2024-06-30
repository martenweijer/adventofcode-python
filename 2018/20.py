import sys
from collections import *

sys.setrecursionlimit(1500000)

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

directions=[(0,-1),(-1,0),(0,1),(1,0)]
LEFT,UP,RIGHT,DOWN=0,1,2,3

DOOR,ROOM,UNKNOWN,WALL=0,1,2,3
grid={}
line=lines[0][1:-1]
row,col=0,0
grid[(row,col)]=UNKNOWN
arr=deque()
for c in line:
    if c=='N':
        row-=1
        grid[(row,col)]=DOOR
        row-=1
        grid[(row,col)]=ROOM
    elif c=='S':
        row+=1
        grid[(row,col)]=DOOR
        row+=1
        grid[(row,col)]=ROOM
    elif c=='E':
        col+=1
        grid[(row,col)]=DOOR
        col+=1
        grid[(row,col)]=ROOM
    elif c=='W':
        col-=1
        grid[(row,col)]=DOOR
        col-=1
        grid[(row,col)]=ROOM
    elif c=='(':
        arr.append((row,col))
    elif c==')':
        row,col=arr.pop()
    elif c=='|':
        row,col=arr[-1]

Q=deque([(0,0)])
seen={(0,0)}
res=0
v=0
while Q:
    res+=1
    for _ in range(len(Q)):
        row,col=Q.popleft()
        for x,y in directions:
            dr,dc=row+x,col+y
            if (dr,dc) in grid and grid[(dr,dc)]==DOOR:
                dr+=x
                dc+=y
                if (dr,dc) not in seen:
                    Q.append((dr,dc))
                    seen.add((dr,dc))
                    if res>=1000:
                        v+=1
print(res-1)
print(v)
