a = int(input("ENTER THE NUMBER: "))
b = int(input("ENTER THE NUMBER: "))
c=0
def swap(a, b): 
    c = b 
    b = a
    a = c
    print("a", a)
    print("b", b)
swap(a, b)    