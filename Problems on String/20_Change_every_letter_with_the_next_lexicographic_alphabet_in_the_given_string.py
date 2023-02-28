# Change every letter with the next lexicographic alphabet in the given string
a = "abcdxyz"
a_list = list(a)
for i in range(0, len(a)):
    if a_list[i] == 'z':
        a_list[i] = 'a'
    else:
        a_list[i] = chr(ord(a[i])+1)    

result = ''
for j in a_list:
    result+=j
print(result)
