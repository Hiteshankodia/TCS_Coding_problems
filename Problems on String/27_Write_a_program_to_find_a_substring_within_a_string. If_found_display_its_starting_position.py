#Write a program to find a substring within a string. If found display its starting position
#Input: str1 = "takeuforward"
#       str2 = “forward”
#Output: 5 
str1 = 'takeuforward' 
str2 = 'forward' 
 
if str2 in str1:
    print(str1.find(str2))

else:
    print("NO!")