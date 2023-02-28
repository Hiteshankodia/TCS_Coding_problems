# Leap Year or not
# Check if the year is divisible by 4 or 400 but not by 100 then it is a leap year.

year = 2001
if ((year%4 ==0) or (year %400 == 0) and not(year % 100 == 0)):
    print("LEAP YEAR!")

else:
    print("NOT A LEAP YEAR!")
    
    