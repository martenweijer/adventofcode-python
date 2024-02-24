import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

D={'a':0,'b':0,'c':0,'d':0}
i=0
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
    i+=1
print(D['a'])

D={'a':0,'b':0,'c':1,'d':0}
i=0
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
    i+=1
print(D['a'])
