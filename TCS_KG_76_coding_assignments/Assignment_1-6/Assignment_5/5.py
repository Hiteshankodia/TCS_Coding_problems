# leap year 
year = 1900
if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 ==0)):
    print("LEAP YEAR!")
else:
    print("NOT A LEAP YEAR!")