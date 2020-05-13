t = list()

while True:
    inp = input('Enter list element or done for ending list: ')
    if inp=='done' :break
    t.append(inp)
t = t[1:len(t)-1]
