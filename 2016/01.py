import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')
R=len(lines)
C=len(lines[0])
grid=[list(line) for line in lines]

pos=[0,0]
dir=0
for d in L.split(', '):
    k,v=d[0],int(d[1:])
    dir+=1 if k=='R' else -1
    dir=(dir+4)%4
    if dir==0:
        pos[0]-=v
    elif dir==1:
        pos[1]+=v
    elif dir==2:
        pos[0]+=v
    elif dir==3:
        pos[1]-=v
res=abs(pos[0])+abs(pos[1])
print(res)

pos=[0,0]
dir=0
S=set()
for d in L.split(', '):
    k,v=d[0],int(d[1:])
    dir+=1 if k=='R' else -1
    dir=(dir+4)%4
    first,min=dir==0 or dir==2,dir==0 or dir==3
    for i in range(1,v+1):
        if first:
            pos[0]+=1 if not min else -1
        else:
            pos[1]+=1 if not min else -1
        t=(pos[0],pos[1])
        if t in S:
            res=abs(pos[0])+abs(pos[1])
            print(res)
            break
        S.add(t)
    else:
        continue
    break
