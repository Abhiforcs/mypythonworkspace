fhand = open(input("Enter file name: "))

schools = dict()

for ln in fhand:
    if not ln.startswith('From '): continue
    ln = ln.split()
    mailer = ln[1]
    pos = mailer.find('@')
    school = mailer[pos+1:]
    schools[school] = schools.get(school,0) + 1
print(schools)
