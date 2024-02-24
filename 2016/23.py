import sys

L=open(sys.argv[1]).read().strip()

def get(v):
    if v in D:
        return D[v]
    return int(v)

def f():
    i=0
    while i<len(lines):
        arr=lines[i]

        if i==4:
            D['a']+=D['b']*D['d']
            i=10
            continue

        if arr[0]=='cpy':
            D[arr[2]]=get(arr[1])
        elif arr[0]=='inc':
            D[arr[1]]+=1
        elif arr[0]=='dec':
            D[arr[1]]-=1
        elif arr[0]=='jnz':
            x,y=get(arr[1]),get(arr[2])
            if x!=0:
                i+=y
                continue
        elif arr[0]=='tgl':
            v=i+get(arr[1])
            if v<len(lines):
                if lines[v][0]=='cpy':
                    lines[v][0]='jnz'
                elif lines[v][0]=='jnz':
                    lines[v][0]='cpy'
                elif lines[v][0]=='inc':
                    lines[v][0]='dec'
                elif lines[v][0]=='dec':
                    lines[v][0]='inc'
                elif lines[v][0]=='tgl':
                    lines[v][0]='inc'
        i+=1

lines=[line.split() for line in L.split('\n')]
D={'a':7,'b':0,'c':0,'d':0}
f()
print(D['a'])

lines=[line.split() for line in L.split('\n')]
D={'a':12,'b':0,'c':0,'d':0}
f()
print(D['a'])
