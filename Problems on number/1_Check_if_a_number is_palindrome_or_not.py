i = int(input("ENTER THE NUMBER"))
x = i 
rev = 0 
while(i>0):
    rev = (rev*10) + i % 10
    i = i//10

if (x == rev):
    print('PALIDROME!')
else:
    print("not a palidrome")        