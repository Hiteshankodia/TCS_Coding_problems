#Strong Number 
n = 145 
result = 0
for i in str(n):
    i = int(i)
    b = 1
    for i in range(1, int(i+1)):
        b *= i 
    result+=b 
print(result)    