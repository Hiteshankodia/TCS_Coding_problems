'''
input: n = 6 
Output: = 2 
Explaination: binary representaion of 6 is 110 
so count of 1 is 2 '''

n = int(input("Enter the number:"))
bin = []
while not(n== 0):
    bin.append(n%2)
    n = n//2
count = 0
for i in bin:
    if i == 1:
        count+=1 
print(count)        