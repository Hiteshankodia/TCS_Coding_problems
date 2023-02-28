#Write a program to find the largest word in a given string.
string = "MICROSOFT DOCS"
string_list = string.split()

a = len(string_list[0])
for i in string_list:
    count = 0 
    length = len(i)
    if length <= a:
        length = a

for i in string_list:
    if len(i) == length:
        print(i)