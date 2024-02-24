import sys
from hashlib import md5

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=[]
s=L
i=0
for _ in range(8):
    h=''
    while not h.startswith('00000'):
        h=md5((s+str(i)).encode('utf-8')).hexdigest()
        i+=1
    res.append(h[5])
print(''.join(res))

res=['0' for _ in range(8)]
i=0
S=set()
while len(S)<8:
    h=''
    while not h.startswith('00000'):
        h=md5((s+str(i)).encode('utf-8')).hexdigest()
        i+=1
    if '0'<=h[5]<='7' and h[5] not in S:
        S.add(h[5])
        res[int(h[5])]=h[6]
print(''.join(res))
