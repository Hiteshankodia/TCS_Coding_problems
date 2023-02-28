# Example 1:
# Input: N = 102003
# Output: 112113
# Explanation: The 2nd,4th and 5th position from left contain 0.The resultant integer has replaced the 0’s in those  positions with 1.

# num = int(input("ENTER THE NUMBER:"))
n = 102003
result = ''
for i in str(102003):
    if i == '0':
        i = '1' 
    elif i == '1':
        i = '0' 
    result +=i  
print(result)
