import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=[]
grid=[[1,2,3],[4,5,6],[7,8,9]]
for line in lines:
    r,c=1,1
    for k in line:
        if k=='U':
            r-=1
        if k=='L':
            c-=1
        if k=='R':
            c+=1
        if k=='D':
            r+=1
        r=max(0,min(2,r))
        c=max(0,min(2,c))
    res.append(str(grid[r][c]))
print(''.join(res))

res=[]
grid=[
    ['0','0','0','0','0','0','0'],
    ['0','0','0','1','0','0','0'],
    ['0','0','2','3','4','0','0'],
    ['0','5','6','7','8','9','0'],
    ['0','0','A','B','C','0','0'],
    ['0','0','0','D','0','0','0'],
    ['0','0','0','0','0','0','0'],
]
for line in lines:
    row,col=3,1
    r,c=row,col
    for k in line:
        if k=='U':
            r-=1
        if k=='L':
            c-=1
        if k=='R':
            c+=1
        if k=='D':
            r+=1
        if grid[r][c]!='0':
            row,col=r,c
        r,c=row,col
    res.append(grid[r][c])
print(''.join(res))
