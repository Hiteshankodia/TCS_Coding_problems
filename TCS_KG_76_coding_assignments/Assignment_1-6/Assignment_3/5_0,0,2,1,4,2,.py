# 0,0,2,1,4,2,6,3,8,4,10,5,12,6,14,7,16,8 
a = [] 
b = []
x = 0
y = 0
for i in range(1,10):
    a.append(x)
    x = 2*i 
for i in range(1,10):
    b.append(y)
    y += 1
c=[]
for i in range(0,len(a)):
    c.append(a[i])
    c.append(b[i])    
n = int(input("ENTERT TEHE NUMBER: "))
print(c[n])