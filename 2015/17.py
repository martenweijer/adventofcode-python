import math
import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

A=[]
for line in lines:
    A.append(int(line))
A.sort(reverse=True)

def dfs(i,sum):
    if sum==150:
        return 1
    if sum>150 or i==len(A):
        return 0
    return dfs(i+1,sum)+dfs(i+1,sum+A[i])
print(dfs(0,0))

def dfs(i,sum,path):
    if sum==150:
        paths.append(path.copy())
        return 1
    if sum>150 or i==len(A):
        return 0
    return dfs(i+1,sum,path)+dfs(i+1,sum+A[i],path+[A[i]])

paths=[]
dfs(0,0,[])
least=math.inf
counter=0
for path in paths:
    if len(path)<least:
        least=len(path)
        counter=0
    if least==len(path):
        counter+=1
print(counter)
