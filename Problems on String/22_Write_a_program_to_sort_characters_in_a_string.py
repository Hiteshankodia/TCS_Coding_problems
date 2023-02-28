#Write a program to sort characters in a string

string = "bfhfsafufqwr"
string_list = list(string)
string_list.sort()

resut ='' 
for i in string_list:
    resut+=i
print(resut)  