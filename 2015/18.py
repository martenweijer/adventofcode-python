import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')
R=len(lines)
C=len(lines[0])

rows,cols=[-1,0,1],[-1,0,1]

def f(grid):
    arr=[r[:] for r in grid]
    for r in range(R):
        for c in range(C):
            count=0
            for dx in rows:
                for dy in cols:
                    dr,dc=r+dx,c+dy
                    if 0<=dr<R and 0<=dc<C and grid[dr][dc]=='#':
                        count+=1
            if grid[r][c]=='#':
                arr[r][c]='#' if 3<=count<=4 else '.'
            elif grid[r][c]=='.':
                arr[r][c]='#' if count==3 else '.'
    return arr

grid=[list(line) for line in lines]
for i in range(100):
    grid=f(grid)
res=sum(r.count('#') for r in grid)
print(res)

grid=[list(line) for line in lines]
for i in range(100):
    grid=f(grid)
    grid[0][0]='#'
    grid[R-1][0]='#'
    grid[R-1][C-1]='#'
    grid[0][C-1]='#'
res=sum(r.count('#') for r in grid)
print(res)
