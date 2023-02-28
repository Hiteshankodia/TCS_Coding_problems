#resverse a string 
a = input()
result=''
for i in range(len(a)-1, -1, -1):
    result += a[i]
print(result)    
