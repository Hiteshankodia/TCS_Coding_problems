# 1,1,2,3,4,9,8,27,16,81,32.....
N = int(input("ENTER THE INDEX NUMBER: ")) 
list2 = []
list1 = []
for i in range(0,20):
    list1.append(2**i)

for i in range(0,20):
    list2.append(3**i)
list3 =[]
for i in range(0,len(list1)):
    list3.append(list1[i])
    list3.append(list2[i])

print(list3[N-1])