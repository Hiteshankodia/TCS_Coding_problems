#Write a program to find second last occurence of the number in array 
 
a = [1,2,3,4,5,5,6,5,6]
f = 5 
indexes = []
count = 0 
for i in a:
    if i == f:
        indexes.append(count)
    count += 1 

print(indexes[-2])    