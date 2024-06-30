import itertools
import sys
from collections import *

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
a,b=0,0
for line in lines:
    C=Counter(line)
    values=C.values()
    if 2 in values:
        a+=1
    if 3 in values:
        b+=1
print(a*b)

for a,b in itertools.combinations(lines,2):
    count=0
    res=''
    for j in range(len(a)):
        if a[j]!=b[j]:
            count+=1
        else:
            res+=a[j]
    if count==1:
        print(res)
