import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

def f(start):
    D={'a':start,'b':0,'c':0,'d':0}
    i=0
    res=[]
    while i<len(lines):
        arr=lines[i].split()
        if arr[0]=='cpy':
            v=arr[1]
            if 'a'<=v<='z':
                D[arr[2]]=D[v]
            else:
                D[arr[2]]=int(v)
        elif arr[0]=='inc':
            D[arr[1]]+=1
        elif arr[0]=='dec':
            D[arr[1]]-=1
        elif arr[0]=='jnz':
            x,y=arr[1],int(arr[2])
            v=D[x] if x in D else int(x)
            if v!=0:
                i+=y
                continue
        elif arr[0]=='out':
            res.append(D[arr[1]])
        i+=1
        if len(res)==24:
            return res

for i in range(1000):
    res=f(i)
    if res==[0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]:
        print(i)
        break
