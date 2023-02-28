
#Remove all duplicates from the input string. 
string = input("ENTER THE INPUT: ")
string_set = set(string)
result =''
for i in string_set:
    result+=i
print(result)

