a = 'how' 
b = '999' 
c = 'you' 
vowels = ['a', 'e','i' ,'o', 'u']
a_list = list(a)
for i in range(0,len(a_list)):
    if a_list[i] in vowels:
        a_list[i] = "*"
b_list = list(b)
for i in range(0, len(b_list)):
    if not(b_list[i] in vowels) and type(i) == 'str':
        b_list[i] = "@"

c = c.upper()
result = ''
for i in a_list:
    result+=i
for i in b_list:
    result+=i 
result = result+c 
print(result)