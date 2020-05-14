fhand = open(input('Enter file name: '))

lines = fhand.read()
lines = lines.split()

dty = dict()

for word in lines:
    dty[word] = len(word)
print(dty)
