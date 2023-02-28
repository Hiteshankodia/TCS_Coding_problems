# factorial of n
#input = 5 
#output = 120
n= 5
fact = 1
for i in range(1,n):
    fact += fact* i 
    
print(fact)    
    