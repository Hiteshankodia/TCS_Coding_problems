# print all prime number in between
a = 1 
b = 10 

for i in range(a, b):
    f = 0 
    for j in range(2,i):
        if i%j == 0:
           f = 1 
    if f == 0:
        print(i)