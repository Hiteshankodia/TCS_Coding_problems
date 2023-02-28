# Check Prime
n = 7
def Prime(n):
    for i in range(2, n):
        if i % n == 0:
            print("NOT PRIME!")
            break
        else:    
            b = 1
    if b==1:
        print("PRIME!")

def check(n):
    if n <= 0:
        print("ENTER THE POSITIVE NUMBER:")
    else:
        a = Prime(n)

check(n)        
    