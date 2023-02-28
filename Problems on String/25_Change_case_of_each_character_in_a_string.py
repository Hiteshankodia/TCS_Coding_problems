#Change case of each character in a string

a = "JAVa PYTHon" 
result = ''
for i in a:
    if i.isupper() == True:
        result += i.lower() 
    if i.islower() == True:
        result += i.upper() 
print(result)        