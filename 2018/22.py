import heapq
import sys

sys.setrecursionlimit(1500000)

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

directions=[(0,-1),(-1,0),(0,1),(1,0)]

depth=int(lines[0].split(': ')[1])
X,Y=int(lines[1].split(': ')[1].split(',')[0]),int(lines[1].split(': ')[1].split(',')[1])

grid={}
DP={}

def f(row,col):
    if (row,col) not in grid:
        if (row,col) in [(0,0),(Y,X)]:
            geo=0
        elif row==0:
            geo=col*16807
        elif col==0:
            geo=row*48271
        else:
            geo=f(row-1,col)[1]*f(row,col-1)[1]
        ero=(geo+depth)%20183
        v=ero%3
        grid[(row,col)]=(geo,ero,v)
    return grid[(row,col)]

res=0
for row in range(Y+1):
    for col in range(X+1):
        res+=f(row,col)[2]
print(res)

PQ=[(0,0,0,1)]
seen=set()
while PQ:
    cost,row,col,tool=heapq.heappop(PQ)
    if (row,col,tool) in seen:
        continue
    seen.add((row,col,tool))
    if row==Y and col==X and tool==1:
        print(cost)
        break
    for t in range(3):
        if t!=tool and t!=f(row,col)[2]:
            heapq.heappush(PQ,(cost+7,row,col,t))
    for dx,dy in directions:
        dr,dc=row+dx,col+dy
        if dr>=0 and dc>=0 and f(dr,dc)[2]!=tool:
            heapq.heappush(PQ,(cost+1,dr,dc,tool))
