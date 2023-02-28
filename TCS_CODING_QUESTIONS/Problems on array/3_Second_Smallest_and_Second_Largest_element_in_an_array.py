#Second Smallest and Second Largest element in an array
a=[2,1,3,4,5,6,7]
b=a[0]
for i in a:
    if b>i:
        b = i 
a.remove(b)
c=a[0]
for i in a:
    if c>i:
        c = i 
print("SECOND LOWEST NUMBER:", c)

d=a[0]
for i in a:
    if d<i:
        d = i 
a.remove(d) 

e=a[0]
for i in a:
    if e<i:
        e = i
print("SECOND HIGHEST NUMBER:", e)        

        