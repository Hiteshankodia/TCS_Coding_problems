# 25 in 625(power) last digits are same
num = 25 
power = num * num
a = str(power)
length_num = len(str(num))
result= a[length_num-1:]
        
if int(result) == num :
    print("AUTOMORPHIC NUMBER")
else:
    print("Not")