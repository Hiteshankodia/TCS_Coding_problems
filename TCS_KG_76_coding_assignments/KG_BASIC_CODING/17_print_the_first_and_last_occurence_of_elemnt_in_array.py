#In an array check the first and last of the certain element 
# a = [1,2,3,1,5,5,5,3,2,4,5]
#input = 5 
#output = 4 and 10 

a = [1,2,3,1,5,5,5,3,2,4,5]
n = 5 
first = 0 
last = 0 
f = 0 
for i in range(len(a)): 
    if ((a[i] == n) and (f ==0)):
        first = i
        f = 1 
    if n == a[i]:
        last = i
print(first)
print(last)
        
    