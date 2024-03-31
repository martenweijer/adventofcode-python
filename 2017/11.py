import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

x,y,z=0,0,0
res=0
for d in L.split(','):
    if d=='n':
        x+=1
        z-=1
    elif d=='s':
        x-=1
        z+=1
    elif d=='nw':
        y+=1
        z-=1
    elif d=='ne':
        x+=1
        y-=1
    elif d=='se':
        z+=1
        y-=1
    elif d=='sw':
        x-=1
        y+=1
    res=max(res,(abs(x)+abs(y)+abs(z)+1)//2)
steps=(abs(x)+abs(y)+abs(z)+1)//2
print(steps)
print(res)
