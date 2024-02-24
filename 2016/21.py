import itertools

import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

n=8

def f(arr):
    for line in lines:
        # swap position 3 with position 6
        if line.startswith('swap position'):
            _,_,x,_,_,y=line.split()
            x,y=int(x),int(y)
            arr[x],arr[y]=arr[y],arr[x]
        # swap letter X with letter Y
        elif line.startswith('swap letter'):
            _,_,a,_,_,b=line.split()
            x,y=arr.index(a),arr.index(b)
            arr[x],arr[y]=arr[y],arr[x]
        # rotate left 3 steps
        elif line.startswith('rotate left'):
            steps=int(line.split()[2])
            arr=arr[steps:]+arr[:steps]
        elif line.startswith('rotate right'):
            steps=int(line.split()[2])
            arr=arr[n-steps:]+arr[:n-steps]
        # rotate based on position of letter X
        elif line.startswith('rotate based'):
            c=line.split()[6]
            p=arr.index(c)
            steps=1+p
            if p>=4:
                steps+=1
            steps%=n
            arr=arr[n-steps:]+arr[:n-steps]
        # reverse positions X through Y
        elif line.startswith('reverse positions'):
            x,y=int(line.split()[2]),int(line.split()[4])
            arr=arr[:x]+arr[x:y+1][::-1]+arr[y+1:]
        # move position X to position Y
        elif line.startswith('move position'):
            _,_,x,_,_,y=line.split()
            x,y=int(x),int(y)
            c=arr[x]
            arr=arr[:x]+arr[x+1:]
            arr=arr[:y]+[c]+arr[y:]
    return arr

print(f(list('abcdefgh')))

for p in itertools.permutations(list('afhbgced')):
    p=list(p)
    arr=f(p)
    if arr==list('fbgdceah'):
        print(p)
        break
