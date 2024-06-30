import math

import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
index,n=0,len(lines)
arr=[]
while index<n:
    line=lines[index]
    x=int(line.split('position=<')[1].split(',')[0])
    y=int(line.split('>')[0].split(',')[1])
    a=int(line.split('velocity=<')[1].split(',')[0])
    b=int(line.split('velocity=<')[1].split(',')[1][:-1])
    arr.append((x,y,a,b))
    index+=1

def f(arr):
    distance=0
    x,y=arr[0][0],arr[0][1]
    for a,b,_,_ in arr:
        distance+=abs(x-a)+abs(y-b)
        x+=a
        y+=b
        x=round(x//2)
        y=round(y//2)
    return distance

def work(arr):
    for i in range(len(arr)):
        a,b,c,d=arr[i]
        a+=c
        b+=d
        arr[i]=(a,b,c,d)
    return arr

distance,seconds=math.inf,0
for sec in range(20000):
    arr=work(arr)
    v=f(arr)
    if v<distance:
        distance=v
        seconds=sec+1

arr=[]
index=0
while index<n:
    line=lines[index]
    x=int(line.split('position=<')[1].split(',')[0])
    y=int(line.split('>')[0].split(',')[1])
    a=int(line.split('velocity=<')[1].split(',')[0])
    b=int(line.split('velocity=<')[1].split(',')[1][:-1])
    arr.append((x,y,a,b))
    index+=1

for _ in range(seconds):
    arr=work(arr)

def p(arr):
    x=[x[0] for x in arr]
    y=[x[1] for x in arr]
    lox=abs(min(x))
    loy=abs(min(y))
    sizeX=abs(max(x))-abs(min(x))
    sizeY=abs(max(y))-abs(min(y))
    grid=[[' ']*(sizeX+1) for _ in range(sizeY+1)]
    for a,b,_,_ in arr:
        grid[b-loy][a-lox]='x'
    for row in grid:
        if 'x' in row:
            print(''.join(row))

p(arr)
print(seconds)
