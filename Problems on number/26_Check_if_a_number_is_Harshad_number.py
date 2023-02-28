# 3+7+8=18. 378 is divisible by 18. Therefore 378 is a harshad number.

num = 378
sum_of_digits = 0
for i in str(num):
    sum_of_digits += int(i)
if num % sum_of_digits == 0:
    print("HARSHAD NUMBER OR NIVEL NUMBER")
else:print("NOT!")    
