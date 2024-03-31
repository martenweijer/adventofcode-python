import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
count=0
group=0
garbage=False
skip=False
for c in L:
    if skip:
        skip=False
        continue
    if garbage:
        if c=='>':
            garbage=False
        elif c=='!':
            skip=True
        else:
            count+=1
    else:
        if c=='{':
            group+=1
        elif c=='}':
            res+=group
            group-=1
        elif c=='<':
            garbage=True
        elif c=='!':
            skip=True
print(res)
print(count)
