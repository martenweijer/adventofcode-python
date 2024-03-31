import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
A,B=0,0
for line in lines:
    if A==0:
        A=int(line.split('with ')[1])
    else:
        B=int(line.split('with ')[1])

def fa(v):
    return (v*16807)%2147483647

def fb(v):
    return (v*48271)%2147483647

for i in range(40*1000000):
    A,B=fa(A),fb(B)
    x,y=bin(A)[2:].zfill(32),bin(B)[2:].zfill(32)
    if x[16:]==y[16:]:
        res+=1
print(res)

res=0
A,B=0,0
for line in lines:
    if A==0:
        A=int(line.split('with ')[1])
    else:
        B=int(line.split('with ')[1])
first,second=[],[]
N=5*1000000
while len(first)<N or len(second)<N:
    if len(first)<N:
        A=fa(A)
        if A%4==0:
            first.append(A)
    if len(second)<N:
        B=fb(B)
        if B%8==0:
            second.append(B)
for i,A in enumerate(first):
    if i<len(second):
        B=second[i]
        x,y=bin(A)[2:].zfill(32),bin(B)[2:].zfill(32)
        if x[16:]==y[16:]:
            res+=1
print(res)
