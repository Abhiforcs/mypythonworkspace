def compareTriplets(a, b):
    x=0
    res=[0,0]
    for item in a:
        if item>b[x]:
            res[0]=res[0]+1
        elif item<b[x]:
            res[1]=res[1]+1
        x=x+1
    return res
a=input('Score for a in 3 categories')
b=input('Score for b in 3 categories')
result= compareTriplets(a,b)
print(result)
