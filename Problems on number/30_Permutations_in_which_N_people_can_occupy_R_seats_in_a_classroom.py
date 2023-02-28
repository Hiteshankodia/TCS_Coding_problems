# To permute n people in r seats we have to find the value of n!/(n-r)!.The value of 5!/(5-3)! Is 60.
n=5 
r = 3
def fact(a):
    b=1
    for i in range(1,a+1):
       b = b*i 
    return b   
n_r = n - r 
n_fact = fact(n)
n_r_fact = fact(n_r)
result = n_fact / n_r_fact 
print(int(result))




