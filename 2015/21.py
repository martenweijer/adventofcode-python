import itertools
import math

import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

boss=[]
for line in lines:
    if 'Hit' in line:
        boss.append(int(line.split(': ')[1]))
    elif 'Damage' in line:
        boss.append(int(line.split(': ')[1]))
    elif 'Armor' in line:
        boss.append(int(line.split(': ')[1]))

D=[
    [
        (8,4,0),
        (10,5,0),
        (25,6,0),
        (40,7,0),
        (74,8,0)
    ],
    [
        (13,0,1),
        (31,0,2),
        (53,0,3),
        (75,0,4),
        (102,0,5),
        (0,0,0)
    ],
    [
        (25,1,0),
        (50,2,0),
        (100,3,0),
        (20,0,1),
        (40,0,2),
        (80,0,3),
        (0,0,0),
        (0,0,0)
    ]
]

def f(damage,armor):
    hp=100
    h,d,a=boss
    while hp>0 and h>0:
        h-=max(1,damage-a)
        if h<=0:
            return True
        hp-=max(1,d-armor)
        if hp<=0:
            return False

res=math.inf
for w in D[0]:
    for a in D[1]:
        for r in itertools.combinations(D[2],2):
            cost=w[0]+a[0]+r[0][0]+r[1][0]
            damage=w[1]+a[1]+r[0][1]+r[1][1]
            armor=w[2]+a[2]+r[0][2]+r[1][2]
            if f(damage,armor):
                res=min(res,cost)
print(res)

res=0
for w in D[0]:
    for a in D[1]:
        for r in itertools.combinations(D[2],2):
            cost=w[0]+a[0]+r[0][0]+r[1][0]
            damage=w[1]+a[1]+r[0][1]+r[1][1]
            armor=w[2]+a[2]+r[0][2]+r[1][2]
            if not f(damage,armor):
                res=max(res,cost)
print(res)
