import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')
R=999+1
C=999+1

res=0
D=[[0]*C for _ in range(R)]
for line in lines:
    if line.startswith('toggle'):
        _,a,_,b=line.split()
        x1,x2=[int(x) for x in a.split(',')]
        y1,y2=[int(x) for x in b.split(',')]
        for i in range(x1,y1+1):
            for j in range(x2,y2+1):
                D[i][j]=(D[i][j]+1)%2
    else:
        _,k,a,_,b=line.split()
        v=0 if k=='off' else 1
        x1,x2=[int(x) for x in a.split(',')]
        y1,y2=[int(x) for x in b.split(',')]
        for i in range(x1,y1+1):
            for j in range(x2,y2+1):
                D[i][j]=v
for r in range(R):
    for c in range(C):
        if D[r][c]==1:
            res+=1
print(res)

res=0
D=[[0]*C for _ in range(R)]
for line in lines:
    if line.startswith('toggle'):
        _,a,_,b=line.split()
        x1,x2=[int(x) for x in a.split(',')]
        y1,y2=[int(x) for x in b.split(',')]
        for i in range(x1,y1+1):
            for j in range(x2,y2+1):
                D[i][j]+=2
    else:
        _,k,a,_,b=line.split()
        v=-1 if k=='off' else 1
        x1,x2=[int(x) for x in a.split(',')]
        y1,y2=[int(x) for x in b.split(',')]
        for i in range(x1,y1+1):
            for j in range(x2,y2+1):
                D[i][j]=max(0,D[i][j]+v)
for r in range(R):
    for c in range(C):
        res+=D[r][c]
print(res)
