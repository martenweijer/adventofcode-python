import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

def f(s):
    for i in range(3,len(s)):
        if s[i-3]==s[i] and s[i-2]==s[i-1] and s[i-1]!=s[i]:
            return True
    return False

res=0
for line in lines:
    good,bad=[],[]
    while '[' in line:
        good.append(line.split('[')[0])
        bad.append(line.split('[')[1].split(']')[0])
        line=line[line.find(']')+1:]
    if line:
        good.append(line)
    B=True
    for s in bad:
        if f(s):
            B=False
            break
    if B:
        for s in good:
            if f(s):
                res+=1
                break
print(res)

def f(s):
    S=set()
    for i in range(2,len(s)):
        if s[i-2]==s[i] and s[i-1]!=s[i]:
            S.add(s[i-1]+s[i]+s[i-1])
    return S

res=0
for line in lines:
    good,bad=[],[]
    while '[' in line:
        good.append(line.split('[')[0])
        bad.append(line.split('[')[1].split(']')[0])
        line=line[line.find(']')+1:]
    if line:
        good.append(line)
    S=set()
    for s in bad:
        S.update(f(s))
    B=False
    for v in S:
        if not B:
            for s in good:
                if v in s:
                    res+=1
                    B=True
                    break
print(res)
