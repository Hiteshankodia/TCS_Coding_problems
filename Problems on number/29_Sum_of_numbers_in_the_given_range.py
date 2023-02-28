#Sum of numbers in the given range 
start = int(input("enter the starting range"))
end = int(input("enter the end range"))
result = 0
for i in range(start, end+1):
    result += i
print(result)


