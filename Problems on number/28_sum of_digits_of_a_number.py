#Sum of digits of a number
num = int(input("ENTER THE NUMBER:"))
sum_of_digits = 0
for i in str(num):
    sum_of_digits += int(i)
print(sum_of_digits)    
