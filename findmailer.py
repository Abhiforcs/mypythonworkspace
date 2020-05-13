count = 0
fhand = open(input('Enter the file name to look in: '))

for ln in fhand:
    if ln.startswith('From '):
        words = ln.split()
        print(words[1])
        count = count + 1
print('There were',count,'lines in the file with From as the first word')
