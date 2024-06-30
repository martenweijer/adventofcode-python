import sys
from copy import deepcopy

L=open(sys.argv[1]).read()
lines=L.split('\n')[:-2]

directions=[(0,-1),(-1,0),(0,1),(1,0)]
LEFT,UP,RIGHT,DOWN=0,1,2,3

dirs={'>':RIGHT,'<':LEFT,'^':UP,'v':DOWN}

res=0
index,n=0,len(lines)
G=lines
carts=[]
R,C=len(G),len(G[0])
for row in range(R):
    for col in range(C):
        if G[row][col] in '<>^v':
            carts.append((row,col,dirs[G[row][col]],0))

def f(carts):
    active=set()
    for r,c,_,_ in carts:
        active.add((r,c))
    while True:
        for i in range(len(carts)):
            r,c,d,a=carts[i]
            active.remove((r,c))
            dr,dc=r+directions[d][0],c+directions[d][1]
            v=G[dr][dc]
            assert v!=' '
            if v=='+':
                if a%3==0:
                    d+=3
                    d%=4
                elif a%3==2:
                    d+=1
                    d%=4
                a+=1
            elif v=='\\':
                if d==RIGHT:
                    d=DOWN
                elif d==UP:
                    d=LEFT
                elif d==DOWN:
                    d=RIGHT
                elif d==LEFT:
                    d=UP
                else:
                    raise ValueError
            elif v=='/':
                if d==UP:
                    d=RIGHT
                elif d==LEFT:
                    d=DOWN
                elif d==DOWN:
                    d=LEFT
                elif d==RIGHT:
                    d=UP
                else:
                    raise ValueError
            carts[i]=(dr,dc,d,a)
            if (dr,dc) in active:
                return (dc,dr)
            active.add((dr,dc))

print(f(deepcopy(carts)))

seen={}
active=set()
for i,(r,c,_,_) in enumerate(carts):
    seen[(r,c)]=i
    active.add((r,c))
deleted=set()
while len(deleted)!=len(carts)-1:
    for i in range(len(carts)):
        if i in deleted:
            continue
        r,c,d,a=carts[i]
        del seen[(r,c)]
        dr,dc=r+directions[d][0],c+directions[d][1]
        v=G[dr][dc]
        assert v!=' '
        if v=='+':
            if a%3==0:
                d+=3
                d%=4
            elif a%3==2:
                d+=1
                d%=4
            a+=1
        elif v=='\\':
            if d==RIGHT:
                d=DOWN
            elif d==UP:
                d=LEFT
            elif d==DOWN:
                d=RIGHT
            elif d==LEFT:
                d=UP
            else:
                raise ValueError
        elif v=='/':
            if d==UP:
                d=RIGHT
            elif d==LEFT:
                d=DOWN
            elif d==DOWN:
                d=LEFT
            elif d==RIGHT:
                d=UP
            else:
                raise ValueError
        carts[i]=(dr,dc,d,a)
        if (dr,dc) in seen:
            deleted.add(i)
            deleted.add(seen[(dr,dc)])
        seen[(dr,dc)]=i
    deleting=[]
    for k,v in seen.items():
        if v in deleted:
            deleting.append(k)
    for k in deleting:
        del seen[k]
for k,_ in seen.items():
    print((k[1],k[0]))
