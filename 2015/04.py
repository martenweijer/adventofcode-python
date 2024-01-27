import sys
from hashlib import md5

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
for i in range(1,int(1e9)):
    if md5((L+str(i)).encode('utf-8')).hexdigest().startswith('00000'):
        res=i
        break
print(res)

res=0
for i in range(1,int(1e9)):
    if md5((L+str(i)).encode('utf-8')).hexdigest().startswith('000000'):
        res=i
        break
print(res)
