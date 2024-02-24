import sys

L=open(sys.argv[1]).read().strip()
lines=L.split('\n')

res=0
intervals=[]
for line in lines:
    start,end=line.split('-')
    intervals.append((int(start),int(end)))
intervals.sort()

i=0
for number in range(0,4294967295+1):
    if number>intervals[i][1]:
        i+=1
    if number<intervals[i][0]:
        print(number)
        break
    number+=1

res=0
number=0
for start,end in intervals:
    if number<start:
        res+=start-number
        number=end+1
    number=max(number,end+1)
print(res)
