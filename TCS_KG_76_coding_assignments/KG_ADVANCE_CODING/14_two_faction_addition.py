''' Program to add Two Fraction and Display Their sum in reduced form 
input : 1 2 3 2   Output: 2 1 ''' 
a = 1 
b = 2 
c = 3 
d = 2 
ad = a*d 
bc = b*c 
num = ad + bc 
den = b*d 
s = min(num, den)
gcd = 0
for i in range(1,num+1):
    if (num % i == 0) and (den % i == 0):
        gcd = i 

print(int(num / gcd),"/",int(den / gcd))
    
