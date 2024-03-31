import sys

L=open(sys.argv[1]).read()
lines=L.split('\n')

res=[]
R,C=len(lines),len(lines[0])
row,col=0,0
direction='D'
for c in range(C):
    if lines[0][c]=='|':
        col=c
        break

def f(row,col,direction):
    steps=0
    p=lines[row][col]
    while 0<=row<R and 0<=col<C:
        c=lines[row][col]
        if c==' ':
            return steps
        if c=='+':
            for x,y,d in [[1,0,'D'],[0,1,'R'],[-1,0,'U'],[0,-1,'L']]:
                dr,dc=row+x,col+y
                if lines[dr][dc]!=p and lines[dr][dc]!='+' and lines[dr][dc]!=' ':
                    direction=d
        elif 'A'<=c<='Z':
            res.append(c)
        if direction=='D':
            row+=1
        elif direction=='U':
            row-=1
        elif direction=='L':
            col-=1
        elif direction=='R':
            col+=1
        p=c
        steps+=1

steps=f(row,col,direction)
print(''.join(res))
print(steps)
