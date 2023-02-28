'''write a program to print diamond star pattern, Given a number n, write a program 
to print a diamond shape with 2*n rows
input: 3              input = 5 
output:               output:
                          *           
  *                      ***
 ***                    *****
*****                  *******
 ***                  ********* 
  *                    *******
                        *****
                         ***
                          *                   '''

a = int(input("ENTER THE NUMBER:"))
b=a-1
for i in range(1, a+1):
    print(" " *((a-1)-(i-1)) + ("*" * (i))+ ("*" * (i-1)))
                    
for i in range(a, 0, -1):
    print(" " *((a-1)-(i-1)) + ("*" * (i))+ ("*" * (i-1)))
                    
                    
                    