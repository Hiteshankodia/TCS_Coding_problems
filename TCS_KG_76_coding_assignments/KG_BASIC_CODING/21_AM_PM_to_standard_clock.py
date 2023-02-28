''' input : 09:15:55PM
output: 21:15:55PM
'''
i = '12:15:55PM'
a = ''
if i[-2:] == "PM":
    a = int(i[:2])
    a = 12 + a 
    print(str(a)+i[2:8])
b =0
if i[-2:] == "AM":
    a = int(i[:2])
    b = 12 + a
    if b == 24:
        b = 0
    print(str(b)+i[2:8])
        