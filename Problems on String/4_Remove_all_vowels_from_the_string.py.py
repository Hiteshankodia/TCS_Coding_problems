#Remove all vowels from the string
string = "HELLO HITESH" 
vowels = ['a' , 'e','i', 'o','u']
string = string.lower()
string_list = list(string)
for i in string_list:
    if i in vowels:
        string_list.remove(i) 
result = ''
for i in string_list:
    result += i 

print(result)        
