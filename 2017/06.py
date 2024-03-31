import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

arr=[int(x) for x in L.split()]
seen=set()
res=0

def f(arr):
    hi=0
    for i,v in enumerate(arr):
        if v>arr[hi]:
            hi=i
    v=arr[hi]
    arr[hi]=0
    index=hi+1
    while v>0:
        arr[index%len(arr)]+=1
        index+=1
        v-=1
    return arr

while ','.join(str(x) for x in arr) not in seen:
    seen.add(','.join(str(x) for x in arr))
    arr=f(arr)
    res+=1
print(res)

res=1
key=','.join(str(x) for x in arr)
arr=f(arr)
while ','.join(str(x) for x in arr)!=key:
    arr=f(arr)
    res+=1
print(res)
