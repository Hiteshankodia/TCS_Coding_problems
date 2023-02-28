#Write a program to find the number of integers with exactly 9 divisors 
#input: 100 Output: 2 
# 36 100 
#divisors of 36 - 1, 2, 3, 4, 6, 9, 10, 12, 18,  36
#divisors of 100 - 1, 2, 4, 5, 10, 20, 25, 50, 100 

n = 100 
count = 0
c = 0
a = []
for i in range(1, n+1):
    count = 0 
    for j in range(1, n+1):
        if i % j == 0:
            count += 1
    if count == 9:
        c += 1 
        a.append(i)
print("There are", c, " number ,which are: " )
for i in a:
    print(i)
        
        
        