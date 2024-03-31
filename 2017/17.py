import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

N=int(L)
res=['0']
pos=0
for i in range(1,2017+1):
    pos+=N
    pos%=len(res)
    res=res[:pos+1]+[str(i)]+res[pos+1:]
    pos+=1
print(res[pos+1])

N=int(L)
res=0
length=1
pos=0
for i in range(1,50000000+1):
    pos+=N
    pos%=length
    if pos==0:
        res=i
    length+=1
    pos+=1
print(res)
