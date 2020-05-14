fhand = open(input('Enter file name: '))
d = dict()

for ln in fhand:
    if not ln.startswith('From '): continue
    words = ln.split()
    d[words[1]] = d.get(words[1],0) + 1
l = list()
for key,value in d.items():
    l.append((value,key))
l.sort(reverse = True)
for val,key in l[:1]:print(key,val)
