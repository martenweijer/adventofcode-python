import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

def f(v):
    res=[]
    for i in range(len(v)-1,-1,-1):
        res.append('1' if v[i]=='0' else '0')
    return ''.join(res)

def g(string):
    v=[]
    for i in range(0,len(string),2):
        v.append('1' if string[i]==string[i+1] else '0')
    return ''.join(v)

T=272
s=L
while len(s)<T:
    s=s+'0'+f(s)
s=s[:T]
while len(s)%2==0:
    s=g(s)
print(s)

T=35651584
s=L
while len(s)<T:
    s=s+'0'+f(s)
s=s[:T]
while len(s)%2==0:
    s=g(s)
print(s)
