#LCM of two numbers 
# lcm = a*b / gcd(a,b)
a = 4 
b = 8 
c=min(a,b)
i=0
for i in range(1, c+1):
    if i % c == 0:
        gcd = i 
lcm = int((a*b) / gcd)
print("LCM OF", a , b , " is: ",lcm)