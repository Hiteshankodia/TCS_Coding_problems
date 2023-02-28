'''Q3: Write a Program to find the nth term of the series.
1,1,2,3,4,9,8,27,16,81,32,243,.... 
Input: 5 Output: 4 
Input: 12 Output: 243
'''
c=0
list1 = []
for i in range(0,6):
    c = 2**i
    list1.append(c)
b=0
list2=[]
for i in range(0,6):
    b = 3**i
    list2.append(b)
list3 = []
for i in range(0,len(list1)):
    list3.append(list1[i])
    list3.append(list2[i])
print(list3)

n = 12
print(list3[n-1])
