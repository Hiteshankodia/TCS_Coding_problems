try:
    a = float(input("ENTER THE NUMBER:"))
    b = float(input("ENTER THE NUMBER:"))

    def sum_1(a,b):
        return a+b 
    
    print(sum_1(a, b))
    
except:        
    print("NUMBERS ARE NOT NUMERIC!")