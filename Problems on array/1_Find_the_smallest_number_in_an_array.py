#Find the smallest number in an array
a = [2,3,4,1,5,6,7]
s = a[0] 
for i in a:
    if s>i:
        s=i

print(s)        
        