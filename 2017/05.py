import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
arr=[]
for line in lines:
    arr.append(int(line))
index=0
while 0<=index<len(arr):
    move=arr[index]
    arr[index]+=1
    index+=move
    res+=1
print(res)

res=0
arr=[]
for line in lines:
    arr.append(int(line))
index=0
while 0<=index<len(arr):
    move=arr[index]
    if move<3:
        arr[index]+=1
    else:
        arr[index]-=1
    index+=move
    res+=1
print(res)
