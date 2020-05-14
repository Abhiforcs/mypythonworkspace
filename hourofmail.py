fhand = open(input('Enter file name: '))
d = dict()

for ln in fhand:
    if not ln.startswith('From '): continue
    words = ln.split()
    time = words[5]
    d[time[:2]] = d.get(time[:2],0) + 1

l = list()

for key,val in d.items():
    l.append((val,key))
l.sort()

for val,key in l:
    print(key,val)
