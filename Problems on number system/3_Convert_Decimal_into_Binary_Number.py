#Convert Decimal into Binary Number
#Input: N = 18
#Output: 10010

n = 18
a=[]
while n>0:
    a.append(n%2)
    n = n//2 
    
result =''

for i in range(len(a)-1, -1, -1):
    result += str(a[i])
print(result)    