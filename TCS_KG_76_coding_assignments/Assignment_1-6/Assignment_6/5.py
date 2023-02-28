# Check Plaidrome Number
n = 121 
n_list1 = list(str(n))
a =0 
b=0
for i in range(0, len(n_list1)):
    if n_list1[i] == (n_list1[(len(n_list1)-1)-i]):
        a = 1
    else:
        b=1 
if a == b:
    print("NOT PALIDROME")
else:
    print("PALIDROME")