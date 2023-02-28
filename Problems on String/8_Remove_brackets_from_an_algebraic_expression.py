#Remove brackets from an algebraic expression 
#Input: “a+((b-c)+d)”
#Output: “a+b-c+d” 

string = 'a+((b-c)+d)'
string_list = list(string)
for i in range(len(string), 0, -1): 
    if (string[i-1] == "(" or string[i-1] == ")"):
        string_list.remove(string[i-1]) 
result = '' 
for j in string_list:
    result += j
print(result)






