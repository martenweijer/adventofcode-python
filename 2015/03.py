import sys

L=open(sys.argv[1]).read().strip()

res=set()
d=(0,0)
res.add(d)
for c in L:
    if c=='>':
        d=(d[0],d[1]+1)
    elif c=='<':
        d=(d[0],d[1]-1)
    elif c=='^':
        d=(d[0]-1,d[1])
    elif c=='v':
        d=(d[0]+1,d[1])
    res.add(d)
print(len(res))

res=set()
d1,d2=(0,0),(0,0)
res.add(d1)
res.add(d2)
i=0
for c in L:
    if i%2==0:
        if c=='>':
            d1=(d1[0],d1[1]+1)
        elif c=='<':
            d1=(d1[0],d1[1]-1)
        elif c=='^':
            d1=(d1[0]-1,d1[1])
        elif c=='v':
            d1=(d1[0]+1,d1[1])
    else:
        if c=='>':
            d2=(d2[0],d2[1]+1)
        elif c=='<':
            d2=(d2[0],d2[1]-1)
        elif c=='^':
            d2=(d2[0]-1,d2[1])
        elif c=='v':
            d2=(d2[0]+1,d2[1])
    res.add(d1)
    res.add(d2)
    i+=1
print(len(res))
