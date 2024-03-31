import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

directions=[(0,-1),(-1,0),(0,1),(1,0)]
LEFT,UP,RIGHT,DOWN=0,1,2,3

arr=[0]*12459852*2
v=0
i=0
state='a'
for _ in range(12459852):
    if state=='a':
        if v==0:
            arr[i]=1
            i+=1
            state='b'
        else:
            arr[i]=1
            i-=1
            state='e'
    elif state=='b':
        if v==0:
            arr[i]=1
            i+=1
            state='c'
        else:
            arr[i]=1
            i+=1
            state='f'
    elif state=='c':
        if v==0:
            arr[i]=1
            i-=1
            state='d'
        else:
            arr[i]=0
            i+=1
            state='b'
    elif state=='d':
        if v==0:
            arr[i]=1
            i+=1
            state='e'
        else:
            arr[i]=0
            i-=1
            state='c'
    elif state=='e':
        if v==0:
            arr[i]=1
            i-=1
            state='a'
        else:
            arr[i]=0
            i+=1
            state='d'
    elif state=='f':
        if v==0:
            arr[i]=1
            i+=1
            state='a'
        else:
            arr[i]=1
            i+=1
            state='c'
    v=arr[i]
print(arr.count(1))
