fhand = open(input('Enter file name: '))

d = dict()
mailer = dict()

for ln in fhand:
    if not ln.startswith('From '): continue
    ln = ln.split()
    d[ln[2]] = d.get(ln[2],0) + 1
    mailer[ln[1]] = mailer.get(ln[1],0) + 1

print(d)
print(mailer)

largest = 0

for key in mailer:
    if mailer[key]>largest:
        largest = mailer[key]
        mostmailer = key
print(mostmailer,largest)
