
#Count frequency of each element in an array
a = [1,2,3,4,5,5,5,5,6,6,6]
b = set(a)
count = []
for i in b:
    c=0
    for j in a:
        if i == j:
            c+=1
    count.append(c)
 
b=list(b)
for i in range(0, len(count)):
    print(str(b[i])+" IS APPEAR "+ str(count[i]) +" time")

