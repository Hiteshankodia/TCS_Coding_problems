#Q2. Write a program that determines whether given integer is odd or even 
#and displays the number and description on the same line.
n = int(input("ENTER THE NUMBER: "))

if n % 2 == 0:
    print(str(n) +" THIS NUMBER IS EVEN")
else:
    print(str(n) + "THIS NUMBER IS ODD")