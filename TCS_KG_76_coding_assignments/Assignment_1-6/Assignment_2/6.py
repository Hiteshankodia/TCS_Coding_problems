'''Q6. An electric power distribution company charges its domestic consumers as follows.
Consumption Units Rate of Charge
0-200 Rs.0.50 per unit
201-400 Rs.100 plus Rs.0.65 per unit
401-600 Rs.230 plus Rs.0.80 per unit.
C program that reads the customer number and power consumed and prints the amount to be paid 
by the customer.'''
n = int(input("ENTER THE NUMBER: "))
total = 0 
if (n>=0 and n<=200):
    total = n * 0.50 
elif (n>=201 and n<=400):
    total = 100 + n*0.65
elif (n>=401 and n<=600):
    total = 230 + n*0.80

print("TOTAL IS :", total)        
