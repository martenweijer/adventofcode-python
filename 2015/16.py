import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
A=[]
for line in lines:
    cur=[]
    for s in line.split(','):
        split=s.split()
        v=int(split[-1])
        name=split[-2][:-1]
        cur.append((name,v))
    A.append(cur)

D={
    'children':3,
    'cats':7,
    'samoyeds':2,
    'pomeranians':3,
    'akitas':0,
    'vizslas':0,
    'goldfish':5,
    'trees':3,
    'cars':2,
    'perfumes':1,
}

for i,values in enumerate(A):
    res=True
    for name,v in values:
        if D[name]!=v:
            res=False
    if res:
        print(i+1)

for i,values in enumerate(A):
    res=True
    for name,v in values:
        if name=='cats' or name=='trees':
            if v<=D[name]:
                res=False
        elif name=='pomeranians' or name=='goldfish':
            if v>=D[name]:
                res=False
        else:
            if D[name]!=v:
                res=False
    if res:
        print(i+1)
