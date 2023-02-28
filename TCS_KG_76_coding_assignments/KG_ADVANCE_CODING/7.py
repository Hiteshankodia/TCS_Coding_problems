#Write a code to print the first 1 bit position from right to left
# input: 18 
#output: 2
#input : 19 
#output : 1 

n = int(input("Enter the number:")) 
a =[]
while not(n==0):
    a.append(n%2)
    n = n//2

count = 0 
for i in a:
    count+=1
    if i == 1:
        print(count)
        break