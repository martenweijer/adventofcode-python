import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
nodes={}
for line in lines[2:]:
    node,_,used,avail,_=line.split()
    x=int(node.split('x')[1].split('-')[0])
    y=int(node.split('y')[1])
    nodes[(x,y)]=(int(used[:-1]),int(avail[:-1]))

res=0
for (x,y),(used,avail) in nodes.items():
    for k,v in nodes.items():
        if (x,y)!=k:
            if 0<used<=v[1]:
                res+=1
print(res)

X,Y=35,24
for x in range(X):
    string=''
    for y in range(Y):
        key=(x,y)
        used,avail=nodes[key]
        if used>100:
            string+='|/##  '
        else:
            string+=str(used)+'/'+str(avail)+' '
    print(string)
lowest=(0,0)
zero=(17,22)
target=(35,0)

moves_to_target=17+22+34
moves_target_lowest=34*5+1
print(moves_to_target+moves_target_lowest)
