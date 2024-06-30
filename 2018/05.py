import math
import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

def f(L):
    stop=False
    while not stop:
        stop=True
        s=''
        i=0
        while i<len(L):
            a,b=L[i],L[i+1] if i+1<len(L) else '~'
            if a.lower()==b.lower() and a!=b:
                stop=False
                i+=2
            else:
                s+=a
                i+=1
        L=s
    return len(L)

print(f(L))

res=math.inf
for i in range(26):
    c=chr(ord('a')+i)
    s=L.replace(c,'')
    s=s.replace(c.upper(),'')
    res=min(res,f(s))
print(res)
