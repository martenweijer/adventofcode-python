import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

directions=[(0,-1),(-1,0),(0,1),(1,0)]
LEFT,UP,RIGHT,DOWN=0,1,2,3

res=0
D={}
for c in range(ord('a'),ord('h')+1):
    D[chr(c)]=0

def get(v):
    if v in D:
        return D[v]
    return int(v)

i=0
while i<len(lines):
    line=lines[i]
    if line.startswith('set'):
        _,k,v=line.split()
        D[k]=get(v)
    elif line.startswith('sub'):
        _,k,v=line.split()
        D[k]-=get(v)
    elif line.startswith('mul'):
        res+=1
        _,k,v=line.split()
        D[k]*=get(v)
    elif line.startswith('jnz'):
        _,k,v=line.split()
        if get(k)!=0:
            i+=get(v)
            continue
    i+=1
print(res)

a,b,c,d,e,f,g,h=1,0,0,0,0,0,0,0

b=81
b*=100
b+=100000
c=b
c+=17000

while True:
    f=1
    d=2
    while True:
        if b%d==0:
            f=0

        d+=1
        if d*d>b:
            break
    if f==0:
        h+=1
    g=b
    g-=c
    b+=17
    if g==0:
        break
print(h)
