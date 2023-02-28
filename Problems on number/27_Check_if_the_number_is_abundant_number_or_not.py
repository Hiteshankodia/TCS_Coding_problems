#Check if the number is abundant number or not
#Divisors of 18 are 1,2,3,6,9. 1+2+3+6+9=21,
# Since 21 is greater than 18, 18 is an abundant number.
num = 18 
div = 0
for i in range(1, num):
    if num % i  == 0:
        div += i 
  
if div > num :
    print("abundant number!")
else:
    print("not an abundant number")