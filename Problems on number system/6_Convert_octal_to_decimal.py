
n = str(345)
a= 0
c = 1
length = len(n)
for i in n:
    b = (int(i) * (8**(length-c)))
    a += b
    c += 1
print(a) 