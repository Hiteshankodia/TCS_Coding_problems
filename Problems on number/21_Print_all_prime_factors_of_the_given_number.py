#Factors of a given number
num = 60

for i in range(2, num):
    while(num % i == 0): 
        num = int(num / i) 
        print(i)