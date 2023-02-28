start = int(input("ENTER THE START NUMBER:"))
end = int(input("ENTER THE END NUMBER:"))
i = 0 
for i in range(start, end+1):
    flag = 0 
    for j in range(2, i):
        if (i % j ==0):
            flag = 1 
            break
    if (flag == 0):
        print(i)

