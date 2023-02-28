x = 20 
y = 28 
s = 0
if x>=y:
    s = y 
else:
    s = x 

gcd = 0
for i in range(2, s+1):
    if (x%i == 0) and (y%i == 0):
        gcd = i
        
print(gcd)  