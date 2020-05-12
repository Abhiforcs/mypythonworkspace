count = 0
try:
    filename = input("Enter file name : ")
    fhandle = open(filename)
except:
    if filename=='na na boo boo':
        print('NA NA BOO BOO TO YOU---You have been punk\'d!')
        exit()
    print("No such file found")
    exit()
tofind = input('Enter starting word of line to find: ')

for ln in fhandle:
    if not ln.startswith(tofind):continue
    count = count + 1
print('There are',count,'lines starting with ',tofind,' in ',filename)
