import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

def f(row):
    next=[]
    for i in range(len(row)):
        l,c,r='.' if i==0 else row[i-1],row[i],'.' if i==len(row)-1 else row[i+1]
        if l=='^' and c=='^' and r=='.':
            next.append('^')
        elif l=='.' and c=='^' and r=='^':
            next.append('^')
        elif l=='^' and c=='.' and r=='.':
            next.append('^')
        elif l=='.' and c=='.' and r=='^':
            next.append('^')
        else:
            next.append('.')
    return next

arr=list(L)
res=arr.count('.')
for i in range(400000-1):
    if i==40-1:
        print(res)
    arr=f(arr)
    res+=arr.count('.')
print(res)
