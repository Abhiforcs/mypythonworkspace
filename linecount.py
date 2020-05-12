count = 0

fhandle = open(input("Enter name of the file : "))
for line in fhandle:
    count = count + 1
print('Line Count :',count)
