'''input: 12-03-2006
output: 31
input: 31-11-1996 
output: 30''' 
a = '12-03-2006'
arr_31 = [1,3,5,7,8,10,12]
arr_28 = [2]
arr_30 = [4,6,9,11]

b = a[3:5]
b = int(b)

if b in arr_31:
    print(31)
elif b in arr_30:
    print(30)
elif b in arr_28:
    print(28)


