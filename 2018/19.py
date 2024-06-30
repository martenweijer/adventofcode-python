import sys

sys.setrecursionlimit(1500000)

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

directions=[(0,-1),(-1,0),(0,1),(1,0)]
LEFT,UP,RIGHT,DOWN=0,1,2,3

def addr(a,b,c,r):
    r[c]=r[a]+r[b]

def addi(a,b,c,r):
    r[c]=r[a]+b

def mulr(a,b,c,r):
    r[c]=r[a]*r[b]

def muli(a,b,c,r):
    r[c]=r[a]*b

def banr(a,b,c,r):
    r[c]=r[a]&r[b]

def bani(a,b,c,r):
    r[c]=r[a]&b

def borr(a,b,c,r):
    r[c]=r[a]|r[b]

def bori(a,b,c,r):
    r[c]=r[a]|b

def setr(a,b,c,r):
    r[c]=r[a]

def seti(a,b,c,r):
    r[c]=a

def gtir(a,b,c,r):
    r[c]=1 if a>r[b] else 0

def gtri(a,b,c,r):
    r[c]=1 if r[a]>b else 0

def gtrr(a,b,c,r):
    r[c]=1 if r[a]>r[b] else 0

def eqir(a,b,c,r):
    r[c]=1 if a==r[b] else 0

def eqri(a,b,c,r):
    r[c]=1 if r[a]==b else 0

def eqrr(a,b,c,r):
    r[c]=1 if r[a]==r[b] else 0

index,n=0,len(lines)
R={}
for i in range(5):
    R[i]=0
pointer=int(lines[0].split()[1])
lines=lines[1:]
while R[pointer]<len(lines):
    line=lines[R[pointer]]
    arr=line.split()[1:]
    a,b,c=int(arr[0]),int(arr[1]),int(arr[2])
    if line.startswith('seti'):
        seti(a,b,c,R)
    elif line.startswith('setr'):
        setr(a,b,c,R)
    elif line.startswith('addr'):
        addr(a,b,c,R)
    elif line.startswith('addi'):
        addi(a,b,c,R)
    elif line.startswith('mulr'):
        mulr(a,b,c,R)
    elif line.startswith('muli'):
        muli(a,b,c,R)
    elif line.startswith('banr'):
        banr(a,b,c,R)
    elif line.startswith('bani'):
        bani(a,b,c,R)
    elif line.startswith('borr'):
        borr(a,b,c,R)
    elif line.startswith('bori'):
        bori(a,b,c,R)
    elif line.startswith('gtir'):
        gtir(a,b,c,R)
    elif line.startswith('gtri'):
        gtri(a,b,c,R)
    elif line.startswith('gtrr'):
        gtrr(a,b,c,R)
    elif line.startswith('eqir'):
        eqir(a,b,c,R)
    elif line.startswith('eqri'):
        eqri(a,b,c,R)
    elif line.startswith('eqrr'):
        eqrr(a,b,c,R)
    R[pointer]+=1
print(R[0])

lines=L.split('\n')
index,n=0,len(lines)
R={}
for i in range(5):
    R[i]=0
pointer=int(lines[0].split()[1])
lines=lines[1:]
counter=0
R[0]=1
while R[pointer]<len(lines):
    line=lines[R[pointer]]
    arr=line.split()[1:]
    a,b,c=int(arr[0]),int(arr[1]),int(arr[2])
    if line.startswith('seti'):
        seti(a,b,c,R)
    elif line.startswith('setr'):
        setr(a,b,c,R)
    elif line.startswith('addr'):
        addr(a,b,c,R)
    elif line.startswith('addi'):
        addi(a,b,c,R)
    elif line.startswith('mulr'):
        mulr(a,b,c,R)
    elif line.startswith('muli'):
        muli(a,b,c,R)
    elif line.startswith('banr'):
        banr(a,b,c,R)
    elif line.startswith('bani'):
        bani(a,b,c,R)
    elif line.startswith('borr'):
        borr(a,b,c,R)
    elif line.startswith('bori'):
        bori(a,b,c,R)
    elif line.startswith('gtir'):
        gtir(a,b,c,R)
    elif line.startswith('gtri'):
        gtri(a,b,c,R)
    elif line.startswith('gtrr'):
        gtrr(a,b,c,R)
    elif line.startswith('eqir'):
        eqir(a,b,c,R)
    elif line.startswith('eqri'):
        eqri(a,b,c,R)
    elif line.startswith('eqrr'):
        eqrr(a,b,c,R)
    R[pointer]+=1
    counter+=1
    if counter>=20:
        break
res=0
for i in range(1,R[3]+1):
    if R[3]%i==0:
        res+=i
print(res)
