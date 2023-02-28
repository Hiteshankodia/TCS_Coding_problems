'''input = AY
ontput = 51'''
a = 'YZ'
a = a[::-1]
count = 0 
result = 0 
for i in a:
    if count == 0:
        result += (ord(i) - 64)
        print((ord(i) - 64))
    else:
        result += (ord(i) - 64)*count
    count +=26
    
print(result)