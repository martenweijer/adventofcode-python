import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

def f(s):
    input=[]
    for c in s:
        input.append(ord(c))
    input+=[17,31,73,47,23]

    N=256
    arr=[x for x in range(N)]
    skip=0
    pos=0
    for _ in range(64):
        for v in input:
            l,r=pos,pos+v-1
            while l<r:
                arr[l%N],arr[r%N]=arr[r%N],arr[l%N]
                l+=1
                r-=1
            pos+=v+skip
            skip+=1
    index=0
    A=[]
    while index<N:
        v=0
        for _ in range(16):
            v^=arr[index]
            index+=1
        A.append(v)
    res=''
    for v in A:
        v=hex(v)[2:].zfill(2)
        res+=v
    return res

grid=[]
res=0
for i in range(128):
    v=L+'-'+str(i)
    v=f(v)
    row=''
    for c in v:
        binary=bin(int(c,16))[2:].zfill(4)
        row+=binary
    res+=row.count('1')
    grid.append(list(row))
print(res)

R,C=128,128
res=0

def dfs(r,c):
    if 0<=r<R and 0<=c<C and grid[r][c]=='1':
        grid[r][c]='2'
        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)

for r in range(R):
    for c in range(C):
        if grid[r][c]=='1':
            res+=1
            dfs(r,c)
print(res)
