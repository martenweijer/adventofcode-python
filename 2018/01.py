import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
for line in lines:
    res+=int(line)
print(res)

res=0
seen=set()
i=0
while res not in seen:
    seen.add(res)
    line=lines[i]
    res+=int(line)
    i+=1
    i%=len(lines)
print(res)
