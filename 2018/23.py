import heapq
import sys

sys.setrecursionlimit(1500000)

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

directions=[(0,-1),(-1,0),(0,1),(1,0)]
LEFT,UP,RIGHT,DOWN=0,1,2,3

index,n=0,len(lines)
bots=[]
hi,hibot=0,[]
while index<n:
    line=lines[index]
    B=[int(x) for x in line.split('<')[1].split('>')[0].split(',')]
    r=int(line.split('r=')[1])
    B.append(r)
    bots.append(B)
    if r>hi:
        hi=r
        hibot=B
    index+=1

res=0
for bot in bots:
    if abs(bot[0]-hibot[0])+abs(bot[1]-hibot[1])+abs(bot[2]-hibot[2])<=hi:
        res+=1
print(res)

def diff(x,y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])+abs(x[2]-y[2])

high=max(max(abs(b[i])+b[3] for b in bots) for i in (0,1,2))
power=1
while power<=high:
    power*=2

def f(box,bot):
    d=0
    for i in (0,1,2):
        lo,hi=box[0][i],box[1][i]-1
        d+=abs(bot[i]-lo)+abs(bot[i]-hi)
        d-=hi-lo
    d//=2
    return d<=bot[3]

def g(box):
    return sum(1 for b in bots if f(box,b))

PQ=[(-len(bots),-2*power,3*power,((-power,-power,-power),(power,power,power)))]
while PQ:
    reach,size,dist,box=heapq.heappop(PQ)
    if size==-1:
        print(dist)
        break
    size//=-2
    for dx in [(0,0,0),(0,0,1),(0,1,0),(0,1,1),
               (1,0,0),(1,0,1),(1,1,0),(1,1,1)]:
        b1=tuple(box[0][i]+size*dx[i] for i in range(3))
        b2=tuple(b1[i]+size for i in range(3))
        b=(b1,b2)
        heapq.heappush(PQ,(-g(b),-size,diff(b1,(0,0,0)),b))
