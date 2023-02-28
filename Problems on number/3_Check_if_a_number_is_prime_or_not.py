num = int(input("ENTER THE NUMBER:"))
for i in range(2,num):
    if num % i == 0:
        print("NOT PRIME!")
        break
else:
    print("PRIME!")    