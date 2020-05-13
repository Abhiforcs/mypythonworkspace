fhand = open(input("Enter the name of file: "))
retlist = ''
for ln in fhand:
    words = ln.split()
    for word in words:
        if word in retlist:continue
        retlist = retlist + ' ' + word
retlist =retlist.split()
retlist.sort()
print(retlist)
