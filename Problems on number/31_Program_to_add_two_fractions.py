# Example 1:
# Input: 3/4 + 1/7 
# Output: 25/28
# Explanation: Since 3/4 + 1/7 = 25/28 

a = int(input())
b = int(input())
c = int(input())
d = int(input())

result1 = (a*d) + (b*c)
result2 = (b*d)

print(result1/result2)
print("The result = {}/{}".format(result1,result2))

