import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
arr={}
hi=0
for line in lines:
    i,v=line.split(': ')
    arr[int(i)]=int(v)
    hi=max(hi,int(i))

for step in range(hi+1):
    if step in arr:
        v=arr[step]
        value=(v-1)*2
        if step%value==0:
            res+=(step*v)
print(res)

def f(wait):
    for step in range(hi+1):
        i=step+wait
        if step in arr:
            v=arr[step]
            value=(v-1)*2
            if i%value==0:
                return True
    return False

wait=0
while f(wait):
    wait+=1
print(wait)
