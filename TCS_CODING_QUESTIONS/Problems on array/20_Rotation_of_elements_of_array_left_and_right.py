#Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
#Output: 6 7 1 2 3 4 5
list1 = [1,2,3,4,5,6,7]
k=2
a = len(list1) - k 

list2 = []
for i in range(0, a):
    list2.append(list1[i])

list3 = []
for i in range(5,len(list1)):
    list3.append(list1[i])
for i in list2:
    list3.append(i)
print(list3)    