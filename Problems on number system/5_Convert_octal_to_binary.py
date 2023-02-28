#Convert octal to binary
#Input: 345
#Output: 011100101

n = str(345)
a= 0
c = 1
length = len(n)
for i in n:
    b = (int(i) * (8**(length-c)))
    a += b
    c += 1


n = a
a=[]
while n>0:
    a.append(n%2)
    n = n//2 

r = ''
for i in a:
    r+=str(i)
print(r[::-1])