#Rotate array by K elements – Block Swap Algorithm 
#{3,4,5,1,2}
N = 7
array = [1,2,3,4,5,6,7] 
K=3
one = array[K:]
two = array[:K] 
for i in two:
    one.append(i)
print(one)    

