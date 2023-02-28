#Check if two strings are anagram of each other
#Input: CAT, ACT
#Output: true
#Explanation: Since the count of every letter of both strings are equal.

str1 = "CAT"
str2 = "ACT" 
count1=0
for i in range(0, len(str1)):
    count1 = count1 + ord(str1[i])
print(count1)    
count2 = 0    
for i in range(0, len(str2)):
    count2 = count2 + ord(str2[i])
print(count2)    

if count1 == count2:
    print(True)
else:
    print(False)
    