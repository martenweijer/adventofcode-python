import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

arr=[3,7]
T=int(L)

def f(arr,a,b):
    v1=arr[a]
    v2=arr[b]
    v=v1+v2
    if v>=10:
        arr.append(1)
        arr.append(v%10)
    else:
        arr.append(v)
    n=len(arr)
    return (arr,(a+v1+1)%n,(b+v2+1)%n)

a,b=0,1
for _ in range(T+10):
    arr,a,b=f(arr,a,b)
print(arr[T:T+10])

arr=[3,7]
target=[int(x) for x in list(str(T))]
n=len(target)
a,b=0,1
while True:
    arr,a,b=f(arr,a,b)
    if arr[-n:]==target:
        print(len(arr)-n)
        break
    if arr[-n-1:-1]==target:
        print(len(arr)-n-1)
        break
