#Remove characters from first string present in the second string
#Input: String str1 = “abcdef”
#       String str2 = “cefz”
#Output: abd 
str1 = 'abcdef' 
str2 = 'cefz' 

str1_list = list(str1)
str2_list = list(str2) 

for i in str2_list:
    if i in str1_list:
        str1_list.remove(i) 
result = ''
for i in str1_list:
    result += i
 
print(result)         