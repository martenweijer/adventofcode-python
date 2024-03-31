import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

directions=[(0,-1),(-1,0),(0,1),(1,0)]
LEFT,UP,RIGHT,DOWN=0,1,2,3

res=0
grid={}
for r,line in enumerate(lines):
    for c in range(len(line)):
        if lines[r][c]=='#':
            grid[(r,c)]=True

row,col=(len(lines))//2,(len(lines))//2
direction=UP
for _ in range(10000):
    key=(row,col)
    if key not in grid or not grid[key]:
        res+=1
        grid[key]=True
        direction-=1
        direction+=4
        direction%=4
    else:
        grid[key]=False
        direction+=1
        direction+=4
        direction%=4
    row+=directions[direction][0]
    col+=directions[direction][1]
print(res)

CLEAN,WEAKENED,INFECTED,FLAGGED=0,1,2,3
res=0
grid={}
for r,line in enumerate(lines):
    for c in range(len(line)):
        if lines[r][c]=='#':
            grid[(r,c)]=INFECTED

row,col=(len(lines))//2,(len(lines))//2
direction=UP
for _ in range(10000000):
    key=(row,col)
    if key not in grid:
        grid[key]=CLEAN
    if grid[key]==CLEAN:
        direction-=1
        direction+=4
        direction%=4
    elif grid[key]==WEAKENED:
        res+=1
    elif grid[key]==INFECTED:
        direction+=1
        direction+=4
        direction%=4
    elif grid[key]==FLAGGED:
        direction+=2
        direction%=4
    grid[key]+=1
    grid[key]%=4
    row+=directions[direction][0]
    col+=directions[direction][1]
print(res)
