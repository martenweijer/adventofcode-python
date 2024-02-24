import sys
from copy import deepcopy

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
for line in lines:
    if line.startswith('rect'):
        x,y=line.split()[1].split('x')
        res+=int(x)*int(y)
print(res)

R,C=6,50
grid=[[' ']*C for _ in range(R)]
for line in lines:
    if line.startswith('rect'):
        x,y=line.split()[1].split('x')
        for r in range(int(y)):
            for c in range(int(x)):
                grid[r][c]='x'
    else:
        _,cmd,op,_,v=line.split()
        if cmd=='row':
            row=int(op.split('=')[1])
            copy=deepcopy(grid[row])
            v=int(v)
            for c in range(C):
                k=(C+v+c)%C
                copy[k]=grid[row][c]
            grid[row]=copy
        elif cmd=='column':
            col=int(op.split('=')[1])
            copy=deepcopy(grid)
            v=int(v)
            for r in range(R):
                k=(R+v+r)%R
                copy[k][col]=grid[r][col]
            grid=copy
for r in range(len(grid)):
    for c in range(0,C,5):
        print(''.join(grid[r][c:c+5]),end='')
        print('    ',end='')
    print('')
