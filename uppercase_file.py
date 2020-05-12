fhandle = open(input('Enter File Name : '))
for ln in fhandle:
    ln = ln.rstrip()
    ln = ln.upper()
    print(ln)
print('Done :)')
