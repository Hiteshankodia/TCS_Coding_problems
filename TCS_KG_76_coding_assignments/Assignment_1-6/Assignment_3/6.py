# print The pattern 
# input 3 4 
# Output:
'''
3          
44
555
6666
555
44
3
''' 
a = 3
b = 4
for i in range(1, b+1):
    print(str(a) * i)
    a=a+1
for i in range(b-1,0,-1):
    a=a-1
    print(str(a-1) * i)
        