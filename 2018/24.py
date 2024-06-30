import sys

sys.setrecursionlimit(1500000)

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

def run(boost=0):
    id=0
    immune=[]
    infection=[]
    I=True
    index,n=0,len(lines)
    while index<n:
        line=lines[index]
        if line.startswith('Immune System'):
            I=True
            index+=1
            id=1
            continue
        if line.startswith('Infection'):
            I=False
            index+=1
            id=1
            continue
        if line:
            unit={'id':id,'target':None}
            id+=1
            unit['type']=I
            unit['units']=int(line.split()[0])
            unit['hp']=int(line.split()[4])
            unit['immune']=set()
            unit['weak']=set()
            if '(' in line:
                for s in line.split('(')[1].split(')')[0].split(';'):
                    if 'immune to' in s:
                        for v in s.split('immune to ')[1].split(','):
                            unit['immune'].add(v.strip())
                    if 'weak to' in s:
                        for v in s.split('weak to ')[1].split(','):
                            unit['weak'].add(v.strip())
            arr=line.split('with an attack that does')[1].split()
            unit['damage']=int(arr[0])
            unit['damage_type']=arr[1].strip()
            unit['initiative']=int(arr[5])
            if I:
                immune.append(unit)
            else:
                infection.append(unit)
        index+=1

    for i in immune:
        i['damage']+=boost

    def power(unit):
        return unit['units']*unit['damage']

    def damage(unit,target):
        if unit['damage_type'] in target['immune']:
            return 0
        if unit['damage_type'] in target['weak']:
            return 2*power(unit)
        else:
            return power(unit)

    def g(attacking,defending):
        return (damage(attacking,defending),power(defending),defending['initiative'])

    def battle(immune,infection):
        while not (all(u['units']<=0 for u in immune) or all(u['units']<=0 for u in infection)):
            units=sorted(immune,key=lambda x:(-power(x),-x['initiative']))
            remaining_targets=set(i for i in range(len(infection)) if infection[i]['units']>0)
            for i,t in enumerate(units):
                t['target']=None
                if not remaining_targets:
                    break
                best_target=max(remaining_targets,key=lambda x:g(t,infection[x]))
                if damage(t,infection[best_target])==0:
                    continue
                t['target']=infection[best_target]
                remaining_targets.remove(best_target)

            units=sorted(infection,key=lambda x:(-power(x),-x['initiative']))
            remaining_targets=set(i for i in range(len(immune)) if immune[i]['units']>0)
            for i,t in enumerate(units):
                t['target']=None
                if not remaining_targets:
                    break
                best_target=max(remaining_targets,key=lambda x:g(t,immune[x]))
                if damage(t,immune[best_target])==0:
                    continue
                t['target']=immune[best_target]
                remaining_targets.remove(best_target)

            attacked=False
            arr=immune+infection
            arr.sort(key=lambda x:-x['initiative'])
            for unit in arr:
                if not unit['target']:
                    continue
                if unit['type']:
                    target=infection[unit['target']['id']-1]
                else:
                    target=immune[unit['target']['id']-1]
                d=damage(unit,target)
                d//=target['hp']
                if target['units']<=0 or d<=0:
                    continue
                attacked=True
                target['units']-=d
                target['units']=max(target['units'],0)
            if not attacked:
                return 0,0
        return sum(u['units'] for u in immune),sum(u['units'] for u in infection)

    return battle(immune,infection)

print(max(run(0)))

# print(run(34))
boost=0
v=0
while v==0:
    v,_=run(boost)
    boost+=1
print(v)
