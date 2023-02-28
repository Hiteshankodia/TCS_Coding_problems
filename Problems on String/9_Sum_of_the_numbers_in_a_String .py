#Sum of the numbers in a String 
#numbers are from 48 to 57
string = "123abc"
sum_1 = 0
for i in string:
    if (ord(i)>=48 and ord(i)<=57):
        sum_1 += int(i) 
print(sum_1)        