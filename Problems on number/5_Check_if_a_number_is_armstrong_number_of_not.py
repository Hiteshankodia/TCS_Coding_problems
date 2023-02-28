num = 153 
def check_amstrong(num):
    order = len(str(num))
    sum =0 
    original = num 
    while num >0 :
        digit = num %10
        sum += digit ** order
        num = num // 10
    if sum == original:
        return True
    return False
if check_amstrong(num):
    print("AMSTRONG")   
else:
    print("Not!")    


