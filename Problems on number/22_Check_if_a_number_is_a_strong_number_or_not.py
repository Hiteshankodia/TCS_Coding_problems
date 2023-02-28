# When the sum of factorial of individual digits of a number is equal to the original number the number is called a strong number. 
# Strong number is also known as Krishnamurthi number/Peterson Number. 

n = 145
num = n 
s=0
for i in str(num):
    i = int(i)
    fact = 1 
    for j in range(1, i+1):
        fact = fact * j 
    s = s+fact 
if(s == n):
    print("STRONG NUMBER")
else:
    print("NOT A STRONG NUMBER")    