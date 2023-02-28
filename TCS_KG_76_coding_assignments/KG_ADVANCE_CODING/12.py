#Write a program to merge to sorted array. resultant array must be sorted

a = [5,6,7,8]
b = [1,2,3,4]

list_1 = a+b
def bubblesort(list_1):
    for iter_num in range(len(list_1)-1,0,-1):
        for idx in range(iter_num):
            if list_1[idx]>list_1[idx+1]:
                temp = list_1[idx]
                list_1[idx] = list_1[idx+1]
                list_1[idx+1] = temp

bubblesort(list_1)
print(list_1)          