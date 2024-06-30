import sys
from collections import *

sys.setrecursionlimit(1500000)

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

directions=[(0,-1),(-1,0),(0,1),(1,0)]
LEFT,UP,RIGHT,DOWN=0,1,2,3

res=0
index,n=0,len(lines)

data=[]
while index<n:
    line=lines[index]
    first,rest=line.split(', ')
    v=int(first.split('=')[1])
    i,j=int(rest.split('..')[0].split('=')[1]),int(rest.split('..')[1])
    for x in range(i,j+1):
        if first[0]=='x':
            data.append((v,x))
        else:
            data.append((x,v))
    index+=1

lox=min(data,key=lambda x:x[1])[1]
loy=min(data,key=lambda y:y[0])[0]
hix=max(data,key=lambda x:x[1])[1]
hiy=max(data,key=lambda y:y[0])[0]
loy-=1
hiy+=1

grid=[]
for i in range(hix+1):
    arr=[]
    for j in range(hiy-loy+1):
        arr.append('.')
    grid.append(arr)

grid[0][500-loy]='+'
for (x,y) in data:
    grid[y][x-loy]='#'

Q=deque([(1,500-loy)])
while Q:
    x,y=Q.popleft()
    if grid[x][y]=='.':
        grid[x][y]='|'
    if x==hix:
        continue
    if grid[x+1][y]=='.':
        Q.append((x+1,y))
        continue
    if grid[x+1][y] in ['~','#']:
        if grid[x][y+1]=='.':
            Q.append((x,y+1))
        if grid[x][y-1]=='.':
            Q.append((x,y-1))
        if grid[x][y+1] in ['|','#'] and grid[x][y-1] in ['|','#']:
            flag=True
            tmp=y
            while grid[x][tmp+1] in ['|','~']:
                tmp+=1
            if grid[x][tmp+1]!='#':
                continue
            tmp=y
            while grid[x][tmp-1] in ['|','~']:
                tmp-=1
            if grid[x][tmp-1]!='#':
                continue
            tmp=y
            grid[x][tmp]='~'
            if grid[x-1][tmp]=='|':
                Q.append((x-1,tmp))
            while grid[x][tmp+1] in ['|','~']:
                grid[x][tmp+1]='~'
                tmp+=1
                if grid[x-1][tmp]=='|':
                    Q.append((x-1,tmp))
            while grid[x][tmp-1] in ['|','~']:
                grid[x][tmp-1]='~'
                tmp-=1
                if grid[x-1][tmp]=='|':
                    Q.append((x-1,tmp))

res=0
for x in range(lox,hix+1):
    for y in range(len(grid[0])):
        if grid[x][y] in '|~':
            res+=1
print(res)

res=0
for x in range(lox,hix+1):
    for y in range(len(grid[0])):
        if grid[x][y]=='~':
            res+=1
print(res)
