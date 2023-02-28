# Maximum and Minimum digit in a number

#Maximum and Minimum digit in a number
num = 1234 
num = str(num) 
max_digit = 0 
min_digit = 0
for i in num:
    if max_digit <= int(i):
        max_digit = int(i)
    elif max_digit >= int(i):
        min_digit = int(i)
print("MAX DIGIT IS " ,max_digit)
print("MIN DIGIT IS " ,min_digit)