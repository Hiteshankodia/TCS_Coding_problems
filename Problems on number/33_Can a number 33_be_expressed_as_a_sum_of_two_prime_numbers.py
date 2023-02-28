# +-> We know that prime numbers are always Odd. So a prime number (odd) cannot be written as the sum of 2 odd prime numbers. So either of them has to be 2. 

# -> Now our question boils down to checking whether n-2 && n prime or not. If both hold true return Yes or No
 
n = 11 
def isprime(a): 
    for i in range(2, a):
        if a %  i == 0:
            return True
             

result = (isprime(n) and isprime(n-1)) 
if result == None:
    print(False)
else:
    print(result)          