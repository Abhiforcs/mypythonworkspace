fhandle = open(input("Enter file name : "))

count = 0
sumcnf = 0

for ln in fhandle:
    if not ln.startswith('X-DSPAM-Confidence'): continue
    pos = ln.find('0')
    confi = float(ln[pos:])
    sumcnf = sumcnf + confi
    count = count + 1
print('Average spam confidence: ',sumcnf/count)
