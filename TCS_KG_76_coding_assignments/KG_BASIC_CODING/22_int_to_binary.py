# int into binary 

i = 33 
a = []
while not(i==0):
    a.append(i%2)
    i = i//2
b = ''
for i in range(0, len(a)):
    b+=str(a[len(a)-1-i]) 
print(b)    
    