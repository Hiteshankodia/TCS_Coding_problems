# Power of a number 
num = int(input("ENTER THE NUMBER :"))
pow = int(input("ENTER THE POWER:"))
result = 1
for i in range(1, pow+1):
    result = result * num 
print(result)