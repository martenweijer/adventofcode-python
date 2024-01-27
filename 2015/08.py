import re
import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
for line in lines:
    line=line.strip().lower()
    res+=len(line)
    res-=len(eval(line))
print(res)

res=0
for line in lines:
    line=line.strip().lower()
    res+=len(line)
    line=re.sub(r'\\x[a-f0-9]{2}','V',line)
    line=line.replace('\\\\','V')
    line=line.replace('\\\"','V')
    res-=len(line)-2
print(res)

res=0
for line in lines:
    line=line.strip().lower()
    res-=len(line)
    line=line.replace('\\','VV')
    line=line.replace('\"','VV')
    res+=len(line)+2

print(res)
