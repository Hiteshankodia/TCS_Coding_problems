#Find Non-repeating characters of a String
a = "1234552"
a_set = set(a) 

list1 = []
list2 = []
for i in a:
    if i in list1:
        list2.append(i)
    else:
        list1.append(i)
print(list2)
print(list1)
result = ''
for j in list1:
    if j not in list2:
        result+=j
print(result)       

