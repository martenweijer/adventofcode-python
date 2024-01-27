import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=lines[0]

def f(s):
    s=list(s[::-1])
    i=0
    while s[i]=='z':
        s[i]='a'
        i+=1
    s[i]=chr(ord(s[i])+1)
    return ''.join(s[::-1])

def valid(s):
    for v in ['i','o','l']:
        if v in s:
            return False
    i=1
    c=0
    while i<len(s):
        if s[i]==s[i-1]:
            c+=1
            i+=2
        else:
            i+=1
    if c<2:
        return False
    for i in range(2,len(s)):
        a,b,c=ord(s[i]),ord(s[i-1]),ord(s[i-2])
        if a==(b+1) and b==(c+1):
            return True
    return False

while True:
    res=f(res)
    if valid(res):
        print(res)
        break

while True:
    res=f(res)
    if valid(res):
        print(res)
        break
