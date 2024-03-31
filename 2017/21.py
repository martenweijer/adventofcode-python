import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

patterns={}

def rotate(key):
    return list(zip(*reversed(key)))

def flip(key):
    key=key.split('/')
    res=[]
    for v in key:
        res.append(v[::-1])
    return '/'.join(res)

def f(key):
    res=[]
    key=key.split('/')
    for _ in range(4):
        key=rotate(key)
        k=''
        for i in key:
            for c in i:
                k+=c
            k+='/'
        res.append(k[:-1])
    return res

for i,line in enumerate(lines):
    first,second=line.split(' => ')
    for key in f(first):
        patterns[key]=second.split('/')
    for key in f(flip(first)):
        patterns[key]=second.split('/')
pattern="""
.#.
..#
###
""".split()

def run(pattern):
    n=len(pattern[0])
    if n%2==0:
        copy=[]
        row=0
        for i in range(n//2):
            for j in range(n//2):
                part=pattern[i*2:(i+1)*2]
                part=[x[j*2:(j+1)*2] for x in part]
                key='/'.join(part)
                assert key in patterns
                for index,v in enumerate(patterns[key]):
                    while (row+index)>=len(copy):
                        copy.append('')
                    copy[row+index]+=v
            row+=3
        pattern=copy
    elif n%3==0:
        copy=[]
        row=0
        for i in range(n//3):
            for j in range(n//3):
                part=pattern[i*3:(i+1)*3]
                part=[x[j*3:(j+1)*3] for x in part]
                key='/'.join(part)
                assert key in patterns
                for index,v in enumerate(patterns[key]):
                    while (row+index)>=len(copy):
                        copy.append('')
                    copy[row+index]+=v
            row+=4
        pattern=copy
    else:
        assert False
    return pattern

for _ in range(5):
    pattern=run(pattern)
print(sum(x.count('#') for x in pattern))
for _ in range(18-5):
    pattern=run(pattern)
print(sum(x.count('#') for x in pattern))
