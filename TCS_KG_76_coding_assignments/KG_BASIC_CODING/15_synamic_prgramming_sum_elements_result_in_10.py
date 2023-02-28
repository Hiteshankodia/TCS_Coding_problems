#sum = 10 
#no_of_array-Elemensts = 9 
#array_elements are 0 2 5 7 4 6 10 20-10
#result = array has two elements with given sum 
s = int(input("Enter the sum you wanna see:"))
#a = [0, 2, 5, 7, 4, 6, 10, 20]
b = int(input("ENTER THE TOTAL NUMBER OF ELEMENTS IN THE ARRAY:"))
a = []
h = 0
for i in range(b):
    h = int(input("ENTER THE " +str(i) + "ELEMENT: "))
    a.append(h)
result = []
for i in a:
    for j in a:
        if (i+j) == 10:
            print(i , j)