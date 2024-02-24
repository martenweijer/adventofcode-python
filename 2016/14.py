import hashlib

import sys
from collections import *

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

hash=L

def next(i,times=0):
    s=hashlib.md5((hash+str(i)).encode('utf-8')).hexdigest()
    for i in range(times):
        s=hashlib.md5(s.encode('utf-8')).hexdigest()
    return s

def f(s):
    arr=[]
    for i in range(4,len(s)):
        C=Counter(s[i-4:i+1])
        if len(C)==1:
            arr.append(s[i])
    return arr

def g(s):
    for i in range(2,len(s)):
        C=Counter(s[i-2:i+1])
        if len(C)==1:
            return s[i]

def valid(c,A):
    for arr in A:
        if c in arr:
            return True
    return False

def go(times=0):
    A=deque()
    i,count=0,0
    while count<64:
        s=next(i,times)
        A.append(f(s))
        if i>=1000:
            A.popleft()
            v=g(next(i-1000,times))
            if v:
                if valid(v,A):
                    count+=1
        i+=1
    return i-1001

print(go())
print(go(2016))
