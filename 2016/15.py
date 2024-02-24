import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
A=[]
for line in lines:
    arr=line.split()
    v,p=int(arr[3]),int(arr[11][:-1])
    A.append((v,p))

def f(T):
    for i,(v,p) in enumerate(A):
        s=((T+i+1+p)%v)
        if s!=0:
            return False
    return True

res,i=None,0
while not res:
    if f(i):
        res=i
    i+=1
print(res)

A.append((11,0))
res,i=None,0
while not res:
    if f(i):
        res=i
    i+=1
print(res)
