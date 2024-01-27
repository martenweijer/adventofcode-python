import math
import sys
from copy import deepcopy

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

boss_hp=int(lines[0].split(': ')[1])
boss_power=int(lines[1].split(': ')[1])

def dfs(hp,mana,effects,boss,turn,spend,hard):
    key=(hp,mana,','.join(str(x) for x in effects),boss,turn)
    if key in DP:
        return
    if spend>=res[0]:
        DP.add(key)
        return
    if mana<0:
        DP.add(key)
        return
    effects=deepcopy(effects)
    armor=0
    if effects[0]>0:
        effects[0]-=1
        armor+=7
    if effects[1]>0:
        effects[1]-=1
        boss-=3
    if effects[2]>0:
        effects[2]-=1
        mana+=101

    if boss<=0:
        res[0]=min(res[0],spend)
        DP.add(key)
        return

    if not turn:
        hp-=max(1,boss_power-armor)
        if hp<=0:
            DP.add(key)
            return
        dfs(hp,mana,effects,boss,True,spend,hard)
    else:
        if hard:
            hp-=1
        # magic missle
        dfs(hp,mana-53,effects,boss-4,False,spend+53,hard)
        # drain
        dfs(hp+2,mana-73,effects,boss-2,False,spend+73,hard)
        # shield
        if effects[0]==0:
            A=deepcopy(effects)
            A[0]=6
            dfs(hp,mana-113,A,boss,False,spend+113,hard)
        # poison
        if effects[1]==0:
            A=deepcopy(effects)
            A[1]=6
            dfs(hp,mana-173,A,boss,False,spend+173,hard)
        # recharge
        if effects[2]==0:
            A=deepcopy(effects)
            A[2]=5
            dfs(hp,mana-229,A,boss,False,spend+229,hard)
    DP.add(key)

DP=set()
res=[math.inf]
dfs(50,500,[0,0,0],boss_hp,True,0,False)
print(res)

DP.clear()
res=[math.inf]
dfs(50,500,[0,0,0],boss_hp,True,0,True)
print(res)
