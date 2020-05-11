def count(char,word):
    total=0
    for any in word:
        if any in char:
            total = total + 1
    return total
result = count('a','banana')
print(result)
