#Remove characters from a string except alphabets 
#alphabet characters are from 65 to 90 and 97 to 122 
string = "HELOHdfugf34613489jkfbjf3q9ru328runqwlk;[o;"
string_list = list(string)
for i in string_list:
    if not ((ord(i) >= 65 and ord(i) <= 90) or (ord(i) >=97 and ord(i)<=122)): 
        string_list.remove(i)
result = ''
for i in string_list:
    result += i  
print(result)    