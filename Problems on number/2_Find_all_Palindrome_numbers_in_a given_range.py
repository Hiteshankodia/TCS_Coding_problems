d =0 
rev = 0 
for i in range(1, 101):
    n=i 
    while n>0:
        rev = rev*10 + n%10 
        n = n //10 

    if i == rev:
        print(i)
    rev = 0    