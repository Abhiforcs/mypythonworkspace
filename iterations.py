smallest = None
Sample=[25,30,60,12,5.5,8]
for value in Sample:
    if smallest is None or smallest>value:
        smallest = value
print('Smallest of value is : ',smallest)
