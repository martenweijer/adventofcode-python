import sys

L=open(sys.argv[1]).read().strip()

res=0
for line in L.split('\n'):
    l,w,h=line.split('x')
    l=int(l)
    w=int(w)
    h=int(h)
    A=[l,w,h]
    A.sort()
    k=A[0]*A[1]
    res+=(2*l*w)+(2*w*h)+(2*h*l)+k
print(res)

res=0
for line in L.split('\n'):
    l,w,h=line.split('x')
    l=int(l)
    w=int(w)
    h=int(h)
    A=[l,w,h]
    A.sort()
    k=A[0]+A[1]+A[0]+A[1]
    res+=(l*w*h)+k
print(res)
