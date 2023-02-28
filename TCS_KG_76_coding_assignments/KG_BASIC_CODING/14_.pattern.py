'''input = 5 
Output:
11111
10001
10001
10001
11111
''' 
n = 5 

print("1"*5)
for i in range(n-2):
    print("1"+ "0"*(n-2) + "1")
print("1"*5)    