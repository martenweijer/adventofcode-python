import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

def f(x,y,z):
    x,y,z=int(x),int(y),int(z)
    return x+y>z and x+z>y and y+z>x

res=0
for line in lines:
    x,y,z=line.split()
    if f(x,y,z):
        res+=1
print(res)

res=0
for i in range(2,len(lines),3):
    if f(lines[i-2].split()[0],lines[i-1].split()[0],lines[i].split()[0]):
        res+=1
    if f(lines[i-2].split()[1],lines[i-1].split()[1],lines[i].split()[1]):
        res+=1
    if f(lines[i-2].split()[2],lines[i-1].split()[2],lines[i].split()[2]):
        res+=1
print(res)
