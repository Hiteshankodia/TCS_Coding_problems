#Capitalize first and last character of each word 
string = "take u forward is awesome" 
string_list = list(string)

last = len(string_list)


for i in range(0, len(string_list)):
    if string_list[i] == string_list[0]:
        string_list[i] = string_list[i].upper()
    elif ord(string_list[i]) == ord(" "):
        string_list[i-1] = string_list[i-1].upper()
        string_list[i+1] = string_list[i+1].upper()
    elif i == (last-1):
        string_list[i] = string_list[i].upper()
        
result = ''    
for i in string_list:
    result+=i 
print(result)    

