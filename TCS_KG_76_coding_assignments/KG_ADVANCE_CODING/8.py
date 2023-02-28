'''input: Two integer M and N 
Output: Print the position of rightmost difference bit in binary representaion of number
''' 
n = 52 
m = 4 
a = []
while not(n==0):
    a.append(n%2)
    n = n//2
b = []
while not(m==0):
    b.append(m%2)
    m = m//2
a1 = []

c = min(len(a), len(b))
count = 1

for i in range(1, c):
    count += 1
    if not((a[i]) == (b[i])):
        print(count)
        break
    elif (i == c-1):
        print(count)