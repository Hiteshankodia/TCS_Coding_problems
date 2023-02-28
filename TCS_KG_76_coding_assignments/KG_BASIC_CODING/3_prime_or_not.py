a = int(input("Enter the number: "))

for i in range(2,a):
    if a % i == 0:
        print("Prime")
        break
else:
    print(a**(1/2))