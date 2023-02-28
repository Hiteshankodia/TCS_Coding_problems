#remove elements from sorted list 
a = [1,2,3,4,4]
b = []
for i in a:
    if i in b:
        a.remove(i)
    else:
        b.append(i)
print(a)        