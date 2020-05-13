ls = list()

while True:
    val = input('Enter a number: ')
    try:
        int(val)
        ls.append(val)
    except:
        if val=='done':
            print('Maximum:',max(ls))
            print('Minimum:',min(ls))
            break
        print('Enter only numeric')
        exit()
