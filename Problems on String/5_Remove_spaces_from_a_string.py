#Remove spaces from a string
string = 'Hello My name is hitesh'
string = string.lower()
string_list = list(string)
for i in string_list:
    if i == " ":
        string_list.remove(i)
result = ''
for j in string_list:
    result +=j 
print(result)
        
