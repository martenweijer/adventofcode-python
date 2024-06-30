import sys
from collections import *

sys.setrecursionlimit(1500000)

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

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
pointer=int(lines[0].split()[1])
lines=lines[1:]

def f():
    R={}
    for i in range(6):
        R[i]=0
    C=Counter()
    while R[pointer]<len(lines):
        C[R[pointer]]+=1
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
        if (R[pointer]+2)==30:
            return R[5]
        R[pointer]+=1
    return True
print(f())

def part2():
    R={
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0
    }
    seen=set()
    last=None
    while True:
        R[3]=R[5]|0x10000
        R[5]=8858047
        while True:
            R[2]=R[3]&0xFF
            R[5]+=R[2]
            R[5]&=0xFFFFFF
            R[5]*=65899
            R[5]&=0xFFFFFF

            if 256>R[3]:
                if R[5] in seen:
                    return last
                seen.add(R[5])
                last=R[5]
                break
            R[3]//=256
print(part2())
