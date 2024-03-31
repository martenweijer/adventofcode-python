import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

arr=[chr(c) for c in range(ord('a'),ord('p')+1)]
N=len(arr)

def f(arr):
    for line in L.split(','):
        if line[0]=='s':
            v=int(line[1:])
            arr=arr[N-v:]+arr[:N-v]
        elif line[0]=='x':
            x,y=line[1:].split('/')
            x,y=int(x),int(y)
            arr[x],arr[y]=arr[y],arr[x]
        elif line[0]=='p':
            a,b=line[1:].split('/')
            x,y=arr.index(a),arr.index(b)
            arr[x],arr[y]=arr[y],arr[x]
    return arr

print(''.join(f(arr)))

arr=[chr(c) for c in range(ord('a'),ord('p')+1)]
seen={''.join(arr)}
prev=-1
i=0
while i<1000000000:
    arr=f(arr)
    key=''.join(arr)
    if key in seen:
        if prev!=-1:
            cycle=i-prev
            while i+cycle<1000000000:
                i+=cycle
        prev=i
        seen.clear()
    seen.add(key)
    i+=1
print(''.join(arr))
