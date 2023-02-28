n=10 
even_sum = 0 
odd_sum = 0
for i in range(1,n+1):
    if i % 2 == 0:
        even_sum+=1
    else:
        odd_sum +=1
print("total odd numbers are: ", odd_sum)
print("Total even numbers are: ", even_sum)
