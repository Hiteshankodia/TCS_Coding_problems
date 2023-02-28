# 1,1,2,2,4,4,8,8,16,16,... 
a = []
for i in range(0,20):
    a.append(2**i)
    a.append(2**i) 
print(a)    