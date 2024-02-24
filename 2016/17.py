import hashlib

import sys
from collections import *

L=open(sys.argv[1]).read().strip()

def hash(path):
    path=L+''.join(path)
    hash=hashlib.md5(path.encode()).hexdigest()
    arr=[]
    for i in range(4):
        c=hash[i]
        arr.append('b'<=c<='f')
    return arr

PATHS=['U','D','L','R']
T=(3,3)
first=None
last=0
Q=deque([(0,0,[])])
while Q:
    for _ in range(len(Q)):
        r,c,path=Q.popleft()
        if (r,c)==T:
            if not first:
                first=''.join(path)
            last=len(path)
            continue
        options=hash(path)
        for i,d in enumerate([[-1,0],[1,0],[0,-1],[0,1]]):
            if options[i]:
                dr,dc=r+d[0],c+d[1]
                if 0<=dr<4 and 0<=dc<4:
                    Q.append((dr,dc,path+[PATHS[i]]))
print(first)
print(last)
