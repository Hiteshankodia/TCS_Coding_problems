#Q3.Write a program to find the number of and sum of all
#integers greater than 100 and less than 200 that are divisible by 7.

a = 100
b = 200
result = 0
for i in range(a,b+1):
    if i % 7 == 0:
        result+=i
       
print(result)
    