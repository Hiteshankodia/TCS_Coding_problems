#Code to reverese a String 
string_1 = input("Enter the String:")
rev_string = ''
for i in range(len(string_1)-1,-1,-1):
    print()
    rev_string += string_1[i]
print(rev_string)    