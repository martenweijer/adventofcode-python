import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
D={}
M={}
for line in lines:
    if line.startswith('NOT'):
        _,src,_,dst=line.split()
        M[dst]=('NOT',src,1)
    else:
        if len(line.split())==5:
            src,cmd,nxt,_,dst=line.split()
            M[dst]=(cmd,src,nxt)
        else:
            v,_,dst=line.split()
            D[dst]=v

def f(dst):
    if dst in D:
        return g(D[dst])
    cmd,a,b=M[dst]
    v1=g(a)
    v2=g(b)
    if cmd=='AND':
        return v1&v2
    if cmd=='OR':
        return v1|v2
    if cmd=='LSHIFT':
        return v1<<v2
    if cmd=='RSHIFT':
        return v1>>v2
    if cmd=='NOT':
        return v1^65535
    assert False

def g(v):
    if v in DP:
        return DP[v]
    if str(v).isdigit():
        DP[v]=int(v)
        return DP[v]
    if v in D:
        DP[v]=g(D[v])
        return DP[v]
    DP[v]=int(f(v))
    return DP[v]

DP={}
res=f('a')
print(res)

D['b']=res
DP.clear()
res=f('a')
print(res)
