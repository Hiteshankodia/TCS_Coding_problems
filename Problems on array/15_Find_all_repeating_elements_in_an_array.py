#Find_all_repeating_elements_in_an_array 
a = [1,2,2,2,3,4,5,6,7,7] 
b=[]
c = []
for i in a:
    if i in b:
       c.append(i)
       
    b.append(i) 

c = set(c) 
for j in b:
    if j not in c:
        print(j)
     
   