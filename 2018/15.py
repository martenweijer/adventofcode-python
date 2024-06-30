import sys
from collections import *
from itertools import count

sys.setrecursionlimit(1500000)

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

directions=[(-1,0),(0,-1),(0,1),(1,0)]
UP,LEFT,RIGHT,DOWN=0,1,2,3

grid=[list(row) for row in lines]

R,C=len(grid),len(grid[0])
index=0
scores={}
elves=0
for r in range(R):
    for c in range(C):
        if grid[r][c] in 'GE':
            scores[index]=[200,r,c,grid[r][c],index]
            grid[r][c]=index
            index+=1

def find_move(index):
    _,r,c,type,_=scores[index]
    Q=deque([(r,c,-1,-1)])
    seen={(r,c)}
    res=[]
    while Q and not res:
        for _ in range(len(Q)):
            r,c,x,y=Q.popleft()
            for dx,dy in directions:
                dr,dc=r+dx,c+dy
                if 0<=dr<R and 0<=dc<C and (dr,dc) not in seen:
                    seen.add((dr,dc))
                    target_index=grid[dr][dc]
                    if isinstance(target_index,int):
                        if scores[target_index][3]!=type:
                            if x==-1:
                                return None
                            assert grid[x][y]=='.'
                            res.append((dr,dc,x,y))
                    elif target_index=='.':
                        if x==-1:
                            Q.append((dr,dc,dr,dc))
                        else:
                            Q.append((dr,dc,x,y))
    if res:
        lo=min(res)
        return lo[2:4]

def sorted_players():
    arr=[]
    for _,v in scores.items():
        hp,r,c,_,_=v
        if hp>0:
            arr.append(v)
    arr=sorted(arr,key=lambda x:[x[1],x[2]])
    return arr

def f(elf_power,death=False):
    for turn in count():
        for hp,r,c,type,index in sorted_players():
            if hp<=0:
                continue
            players=sorted_players()
            S=Counter(player[3] for player in players)
            if S['G']==0 or S['E']==0:
                return turn*sum(player[0] for player in players)
            move=find_move(index)
            if move:
                grid[move[0]][move[1]]=grid[r][c]
                grid[r][c]='.'
                r,c=move[0],move[1]
                scores[index][1]=move[0]
                scores[index][2]=move[1]
            targets=[]
            for dx,dy in directions:
                dr,dc=r+dx,c+dy
                if 0<=dr<R and 0<=dc<C:
                    target_index=grid[dr][dc]
                    if isinstance(target_index,int):
                        unit=scores[target_index]
                        if unit[3]!=type:
                            targets.append(unit)
            if targets:
                target=min(targets,key=lambda x:x[0])
                target_index=target[4]
                if type=='E':
                    scores[target_index][0]-=elf_power
                else:
                    scores[target_index][0]-=3
                if scores[target_index][0]<=0:
                    if death and scores[target_index][3]=='E':
                        return
                    _,x,y,_,_=scores[target_index]
                    grid[x][y]='.'

print(f(3))
for power in count(4):
    grid=[list(row) for row in lines]

    R,C=len(grid),len(grid[0])
    index=0
    scores={}
    elves=0
    for r in range(R):
        for c in range(C):
            if grid[r][c] in 'GE':
                scores[index]=[200,r,c,grid[r][c],index]
                grid[r][c]=index
                index+=1

    res=f(power,death=True)
    if res:
        print(res)
        break
