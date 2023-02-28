#Find all repeating elements in an array 
a = [1,2,2,2,3,4,5,6,7,7] 
b=[]
c = []
for i in a:
    if i in b:
       c.append(i)
       
    b.append(i) 
c = set(c) 
for j in c:
    print(j)
   