#Print all the duplicates in the input string.

string = "123455552" 
string_set = set(string)

list1 = []
for i in string:
    if i in list1:
        print(i)
    else:
        list1.append(i)
     
