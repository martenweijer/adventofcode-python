import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
index,n=0,len(lines)
T=int(L)

def f(x,y):
    rack=x+10
    level=rack*y
    level+=T
    level*=rack
    level//=100
    level%=10
    return level-5

grid=[[-1000]*301 for _ in range(301)]
for row in range(300):
    for col in range(300):
        grid[row][col]=f(row,col)

res=0
cell=0
for row in range(1,298):
    for col in range(1,298):
        v=0
        for i in range(3):
            for j in range(3):
                v+=grid[row+i][col+j]
        if v>res:
            res=v
            cell=(row,col)
print(cell)

res=0
cell=0
size=0
for row in range(1,300):
    for col in range(1,300):
        v=0
        for i in range(300):
            if row+i>=300 or col+i>=300:
                break
            for r in range(1,i):
                v+=grid[row+r][col+i]
            for c in range(1,i):
                v+=grid[row+i][col+c]
            v+=grid[row+i][col+i]
            if v>res:
                res=v
                cell=(row+1,col+1)
                size=i
print(cell,size)
