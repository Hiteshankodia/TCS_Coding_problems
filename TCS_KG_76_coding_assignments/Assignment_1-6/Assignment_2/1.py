#Q1. The cost of one type of mobile service is Rs.250 plus Rs.1.25 for each call made 
#over and above 100 calls. Write a program to read calls made and print the bill for customer.
one_type_service = 250 
rs = 1.25 
over = 100
total = 0
n = int(input("ENTER THE NUMBER: "))
if n >= over:
    total = one_type_service + (rs * n)
else:
    total = one_type_service 
print("THE TOTAL OF BILL IS -", total)
