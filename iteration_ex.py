count = 0
sum = 0
number = 0
number = input("Enter a number or done : ")
while number!='done':
    try:
        int(number)
        count = count + 1
        sum = sum + int(number)
    except:
        print('Enter only number or \'done\' keyword')
    number = input("Enter a number or done : ")
print('Total = ',sum)
print('Count = ',count)
print('Average = ',sum/count)
