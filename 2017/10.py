import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

N=256
arr=[x for x in range(N)]
skip=0
pos=0
for v in L.split(','):
    v=int(v)
    l,r=pos,pos+v-1
    while l<r:
        arr[l%N],arr[r%N]=arr[r%N],arr[l%N]
        l+=1
        r-=1
    pos+=v+skip
    skip+=1
print(arr[0]*arr[1])

input=[]
for c in L:
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
    v=hex(v)[2:]
    if len(v)==1:
        v='0'+v
    res+=v
print(res)
