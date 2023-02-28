#Convert decimal to octal
#Input:  17
#Output: 21

n = 17
a=''
while n>0:
   a+= str(n % 8)
   n = n//8

result = a[::-1]
print(int(result))