import sys
from collections import *

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=[defaultdict(int) for _ in range(8)]
for line in lines:
    for i,c in enumerate(line):
        res[i][c]+=1
print(''.join([max(x,key=x.get) for x in res]))
print(''.join([min(x,key=x.get) for x in res]))
