import sys

L=open(sys.argv[1]).read().strip()

res=0
while L:
    i=L.find('(')
    if i==-1:
        res+=len(L)
        break
    cmd=L[i:].split(')')[0][1:]
    res+=i
    x,y=[int(k) for k in cmd.split('x')]
    res+=(x*y)
    L=L[i+len(cmd)+2+x:]
print(res)

L=open(sys.argv[1]).read().strip()

def f(s):
    i=s.find('(')
    if i==-1:
        return len(s)
    cmd=s[i:].split(')')[0][1:]
    x,y=[int(k) for k in cmd.split('x')]
    n=i+len(cmd)+2
    inner=s[n:n+x]
    return i+(f(inner)*y)+f(s[n+x:])

print(f(L))
