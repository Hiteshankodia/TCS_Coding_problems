#Count number of vowels, consonants, spaces in String
#alphabtes is from 65 to 90(capital) and 97 to 122(small)
vowels = ['a', 'e' ,'i','o','u'] 
string = "India won the cricket match" 
v = 0
s = 0
c = 0
string.lower()
for i in string:
    if i in vowels:
        v += 1
    elif i == " ":
        s +=1
    else:
        c += 1 
print('vowels: ', v)
print('Consonants: ', c)
print('White Spaces: ', s)
