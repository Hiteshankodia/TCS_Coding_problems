#Calculate frequency of characters in a string
string = 'takeuforward'
a = list(string) 
a.sort ()
b = set(a) 
count =[]
for i in b:
    c=0
    for j in a:
        if i == j:
            c+=1
    count.append(c)
 
b=list(b)
for i in range(0, len(count)):
    print(str(b[i])+" IS APPEAR "+ str(count[i]) +" time")

