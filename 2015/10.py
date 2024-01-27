import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

def f(s):
    C=''
    i=0
    while i<len(s):
        c,k=s[i],1
        i+=1
        while i<len(s) and s[i]==c:
            i+=1
            k+=1
        C+=str(k)
        C+=c
    return C

res=lines[0]
for _ in range(40):
    res=f(res)
print(len(res))

res=lines[0]
for _ in range(50):
    res=f(res)
print(len(res))
