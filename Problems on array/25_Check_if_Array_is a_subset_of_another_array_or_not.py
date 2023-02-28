#Check if Array is a subset of another array or not
sub = [1,2,3,4]
a = [1,2,3,4,5,6,7,8,9]
length = len(sub)
b=[]
for i in sub:
    if i in a:
        b.append(a) 

if length == len(b):
    print(True)
        