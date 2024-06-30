import sys

sys.setrecursionlimit(1500000)

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

R,C=50,50
moves=[[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]

index,n=0,len(lines)
grid=[]
while index<n:
    line=lines[index]
    grid.append(list(line))
    index+=1

def f(grid):
    arr=[]
    for r in range(R):
        row=[]
        for c in range(C):
            if grid[r][c]=='.':
                count=0
                for x,y in moves:
                    dr,dc=r+x,c+y
                    if 0<=dr<R and 0<=dc<C and grid[dr][dc]=='|':
                        count+=1
                if count>=3:
                    row.append('|')
                else:
                    row.append('.')
            elif grid[r][c]=='|':
                count=0
                for x,y in moves:
                    dr,dc=r+x,c+y
                    if 0<=dr<R and 0<=dc<C and grid[dr][dc]=='#':
                        count+=1
                if count>=3:
                    row.append('#')
                else:
                    row.append('|')
            elif grid[r][c]=='#':
                count,kount=0,0
                for x,y in moves:
                    dr,dc=r+x,c+y
                    if 0<=dr<R and 0<=dc<C:
                        if grid[dr][dc]=='#':
                            count+=1
                        if grid[dr][dc]=='|':
                            kount+=1
                if count>=1 and kount>=1:
                    row.append('#')
                else:
                    row.append('.')
        arr.append(row)
    return arr

def k(arr):
    key=''
    for r in range(R):
        key+=''.join(arr[r])
    return key

def calc(arr):
    wood,lumber=0,0
    for r in range(R):
        for c in range(C):
            if arr[r][c]=='|':
                wood+=1
            if arr[r][c]=='#':
                lumber+=1
    return wood*lumber

G={}
T=1000000000
i=0
while i<T:
    grid=f(grid)
    key=k(grid)
    if key in G:
        diff=i-G[key]
        while i+diff<1000000000:
            i+=diff
    G[key]=i
    i+=1
    if i==10:
        print(calc(grid))

print(calc(grid))
