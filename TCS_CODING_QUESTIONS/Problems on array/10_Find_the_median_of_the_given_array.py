#Find the median of the given array 
a = [1,2,3,4,5,6] 

if len(a) % 2 == 1: 
    mid = int(len(a)/2)
    print(a[mid])
    
else:
    mid_1 = int(len(a)/2) 
    mid_2 = int(len(a)/2)-1 
    mid = (a[mid_2] +  a[mid_1])/2
    print(mid) 
  
    