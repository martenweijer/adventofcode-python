import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
for line in lines:
    A=['ab','cd','pq','xy']
    B=False
    for a in A:
        if a in line:
            B=True
            break
    if B:
        continue
    V='aeiou'
    c=0
    for v in V:
        c+=line.count(v)
        if c>=3:
            break
    if c<3:
        continue

    G=False
    for i in range(1,len(line)):
        if line[i]==line[i-1]:
            G=True
            break
    if G:
        res+=1
print(res)

res=0
for line in lines:
    G=False
    for i in range(2,len(line)):
        if line[i]==line[i-2]:
            G=True
            break
    if not G:
        continue
    B=False
    for i in range(2,len(line)):
        s=line[i-2:i]
        if s in line[i:]:
            B=True
            break
    if B:
        res+=1
print(res)
