import sys

L=open(sys.argv[1]).read().strip()

res=L.count('(')-L.count(')')
print(res)

res=0
v=0
for c in L:
    res+=1
    if c=='(':
        v+=1
    elif c==')':
        v-=1
    if v<0:
        break
print(res)
