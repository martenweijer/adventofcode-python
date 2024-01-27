import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

instructions=[]
for line in lines:
    s=line.split()
    if s[0]=='jio' or s[0]=='jie':
        instructions.append((s[0],s[1][:-1],s[2][0],s[2][1:]))
    else:
        instructions.append((s[0],s[1]))

def f(a,b):
    i=0
    while i<len(instructions):
        cmd=instructions[i]
        if cmd[0]=='jio' or cmd[0]=='jie':
            operation,register,op,value=cmd
            if operation=='jio':
                v=a if register=='a' else b
                if v[0]==1:
                    i+=int(value) if op=='+' else -int(value)
                    continue
            if operation=='jie':
                v=a if register=='a' else b
                if v[0]%2==0:
                    i+=int(value) if op=='+' else -int(value)
                    continue
        else:
            operation,register=cmd
            v=a if register=='a' else b
            if operation=='tpl':
                v[0]*=3
            elif operation=='hlf':
                v[0]//=2
            elif operation=='inc':
                v[0]+=1
            elif operation=='jmp':
                op=register[0]
                v=int(register[1:])
                i+=v if op=='+' else -v
                continue
        i+=1

a,b=[0],[0]
f(a,b)
print(b[0])

a,b=[1],[0]
f(a,b)
print(b[0])
