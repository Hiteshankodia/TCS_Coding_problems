#Find the largest number in an array 
length = int(input('ENTER THE LENGTH OF ARRAY:'))
a = []
b=0
for i in range(0, length):
    b = int(input("ENTER THE ARRAY ELEMENT AT INDEX"))
    a.append(b)
print(a)
c=a[0]
for j in a:
    if j > c:
        c = j 
print(j)        