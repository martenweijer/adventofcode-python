import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')


def f(v):
    if isinstance(v,list):
        for k in v:
            f(k)
    elif isinstance(v,dict):
        for k,v in v.items():
            f(k)
            f(v)
    elif isinstance(v,str):
        try:
            res[0]+=int(v)
        except:
            pass
    elif isinstance(v,int):
        res[0]+=v

res=[0]
for line in lines:
    j=eval(line)
    f(j)
print(res)

def f(v):
    if isinstance(v,list):
        for k in v:
            f(k)
    elif isinstance(v,dict):
        if 'red' not in v:
            for k,i in v.items():
                if i=='red':
                    return
            for k,v in v.items():
                f(k)
                f(v)
    elif isinstance(v,str):
        try:
            res[0]+=int(v)
        except:
            pass
    elif isinstance(v,int):
        res[0]+=v

res=[0]
for line in lines:
    j=eval(line)
    f(j)
print(res)
