import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

s=lines[0].split()
row,col=int(s[-3][:-1]),int(s[-1][:-1])

v=0
for i in range(0,row-1):
    v+=i

for _ in range(col):
    v+=row
    row+=1

res=20151125
for _ in range(1,v):
    res*=252533
    res%=33554393
print(res)
