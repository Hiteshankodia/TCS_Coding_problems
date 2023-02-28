#Check Leap Year , input = 2016 
#output = Leap Year 

yr = int(input("Enter The Year:"))

if (yr%100 == 0) and (yr % 400 == 0):
    print("Leap Year")
elif (yr % 4 == 0) and not(yr %100 == 0):
    print("Leap Year")
else:
    print("Not A Leap Year!")