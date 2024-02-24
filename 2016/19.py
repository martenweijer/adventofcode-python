import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

T=int(L)
available_players=list(range(T))
while len(available_players)>1:
    arr=[]
    for i in range(0,len(available_players),2):
        arr.append(available_players[i])
    if len(available_players)%2==1:
        arr=arr[1:]
    available_players=arr
print(available_players[0]+1)

class Node:
    def __init__(self,v):
        self.v=v

start=Node(1)
half=None
previous=start
for i in range(2,T+1):
    node=Node(i)
    node.left=previous
    previous.right=node
    previous=node

    if i==T//2+1:
        half=node
previous.right=start
start.left=previous

while T!=1:
    half.left.right=half.right
    half.right.left=half.left

    half=half.right
    if T%2==1:
        half=half.right
    start=start.right

    T-=1
print(start.v)
