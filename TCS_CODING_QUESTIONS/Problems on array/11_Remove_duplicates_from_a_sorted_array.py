#Remove duplicates from a sorted array
a = [1,2,4,3,5,7,7,7,7,6,8,8,9]
a.sort()
b=0 
a = set(a)
print(a)