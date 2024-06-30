import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
index,n=0,len(lines)
T=''
G={}
while index<n:
    line=lines[index]
    if 'state' in line:
        T=line.split(': ')[1]
    elif line:
        src,dst=line.split(' => ')
        G[src]=dst
    index+=1

plants=set()
for i in range(len(T)):
    if T[i]=='#':
        plants.add(i)

def f(arr):
    res=set()
    for i in range(min(arr)-2,max(arr)+3):
        part=''
        for j in range(i-2,i+3):
            part+='#' if j in arr else '.'
        if G[part]=='#':
            res.add(i)
    return res

for _ in range(20):
    plants=f(plants)

print(sum(plants))

prev=0
diff=0
for i in range(1000-20):
    plants=f(plants)
    S=sum(plants)
    diff=S-prev
    prev=S

res=prev+diff*(50000000000-1000)
print(res)
