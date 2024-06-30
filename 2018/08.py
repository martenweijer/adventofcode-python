import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
arr=[int(x) for x in L.split()]

def dfs(i):
    childs=arr[i]
    metadata=arr[i+1]
    i+=2
    if childs==0:
        return (sum(arr[i:i+metadata]),i+metadata)
    v=0
    for _ in range(childs):
        t=dfs(i)
        v+=t[0]
        i=t[1]
    v+=sum(arr[i:i+metadata])
    return (v,i+metadata)

print(dfs(0)[0])

def dfs(i):
    childs=arr[i]
    metadata=arr[i+1]
    i+=2
    if childs==0:
        return (sum(arr[i:i+metadata]),i+metadata)
    v=0
    A=[0]
    for _ in range(childs):
        t=dfs(i)
        A.append(t[0])
        i=t[1]
    for index in arr[i:i+metadata]:
        if 0<index<len(A):
            v+=A[index]
    return (v,i+metadata)

print(dfs(0)[0])
