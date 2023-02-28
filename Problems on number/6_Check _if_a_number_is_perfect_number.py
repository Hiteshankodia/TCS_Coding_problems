#Check if a number is perfect number
#the sum of their proper divisors (1+2+3)

num = 6 
sum_1 = 0
for i in range(1, num):
    if 6 % i == 0:
        sum_1 += i
if sum_1 == num:
    print("PERFECT NUMBER!")