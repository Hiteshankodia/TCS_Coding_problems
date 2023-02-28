#Reverse words in a string 
string = "hitesh ankodia" 
result = ''
for i in range(len(string)-1,-1, -1):
    result += string[i]  
print(result)    