import sys
from collections import defaultdict

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

operations=[addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]

G=defaultdict(set)

def f(registers,expect,after):
    count=0
    a,b,c=expect[1],expect[2],expect[3]
    opcode=expect[0]
    for i,o in enumerate(operations):
        reg=registers[::]
        value=after[c]
        o(a,b,c,reg)
        if reg[c]==value:
            G[opcode].add(i)
            count+=1
    return count>=3

res=0
index,n=0,len(lines)
while index<n:
    line=lines[index]
    if line.startswith('Before'):
        registers=[int(x) for x in line.split('[')[1].split(']')[0].split(',')]
        index+=1
        expect=[int(x) for x in lines[index].split()]
        index+=1
        after=[int(x) for x in lines[index].split('[')[1].split(']')[0].split(',')]
        if f(registers,expect,after):
            res+=1
    index+=1
print(res)

n=len(G)
map={}
while len(map)<n:
    for k in G.keys():
        v=G[k]
        if len(v)==1:
            op=v.pop()
            map[k]=op
            for values in G.values():
                if op in values:
                    values.remove(op)

res=0
index=3174
registers=defaultdict(int)
while index<len(lines):
    line=lines[index]
    if line:
        op,a,b,c=[int(x) for x in line.split()]
        o=map[op]
        operations[o](a,b,c,registers)
    index+=1
print(registers[0])
