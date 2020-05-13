retlist = list()
fhand = open(input("Enter the name of file: "))

for ln in fhand:
    words = ln.split()
    for word in words:
        if word in retlist:continue
        retlist.append(word)

retlist.sort()
print(retlist)
