import sys
from collections import *

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

class Node:
    def __init__(self,v):
        self.v=v

P=int(L.split()[0])
HI=int(L.split()[6])
node=Node(0)
node.left=node
node.right=node

player=1
scores=defaultdict(int)
for i in range(1,(HI*100)+1):
    if i%23==0:
        for _ in range(7):
            node=node.left
        scores[player]+=i+node.v

        node.left.right=node.right
        node.right.left=node.left
        node=node.right
    else:
        node=node.right
        nei=Node(i)
        nei.left=node
        nei.right=node.right
        node.right.left=nei
        node.right=nei

        node=nei
    if i==HI:
        print(max(scores.values()))
    player+=1
    player%=P
print(max(scores.values()))
