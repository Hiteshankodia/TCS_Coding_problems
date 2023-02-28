num1 = 10 
num2 = 20 
a = min(num1,num2)
for i in range(1, a+1):
    if a % i == 0:
        result = i
print(result)