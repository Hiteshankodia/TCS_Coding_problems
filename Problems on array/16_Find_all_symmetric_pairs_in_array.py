#Input: (1,2),(2,1),(3,4),(4,5),(5,4)
#Output: (2,1) (5,4)

a = [(1,2),(2,1),(3,4),(4,5),(5,4)]
sym_pairs = []
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] == a[j][::-1]:
            sym_pairs.append(a[i])
            
result = []
for i in sym_pairs:
    if not i[::-1] in result:
        result.append(i)
    else:
        continue
print(result)    
        
    

            

    
