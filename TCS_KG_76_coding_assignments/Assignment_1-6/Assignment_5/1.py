list1 = []
for i in range(0,20):
    list1.append(2**i)
list2 = []
for i in range(0,20):
    list2.append(3**i)
list3 = []
for i in range(0, len(list1)):
    list3.append(list1[i])
    list3.append(list2[i])
print(list3)    
n = int(input("ENTER THE NUMBER:"))
print(list3[n-1])