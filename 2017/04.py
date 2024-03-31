import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
for line in lines:
    arr=line.split()
    if len(arr)==len(set(arr)):
        res+=1
print(res)

res=0
for line in lines:
    arr=line.split()
    if len(arr)==len(set(arr)):
        words=set()
        valid=True
        for word in arr:
            word=''.join(sorted(list(word)))
            if word in words:
                valid=False
                break
            words.add(word)
        if valid:
            res+=1
print(res)
