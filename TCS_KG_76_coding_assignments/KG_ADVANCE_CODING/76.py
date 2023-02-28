#Given integer N, find the sum of odd numbers and even numbers from 1 to N. 
#input : 5   Output: 9 6  (odd = 9 even = 6)
#input: 6    Output: 9 12 
 
a = 5 
b = 0 
c = 0 
for i in range(a+1):
    if i % 2 == 0:
        b += i 
    elif i % 2 == 1:
        c += i 
print(c,b )        