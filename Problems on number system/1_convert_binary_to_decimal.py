#Convert Binary to Decimal
bin = 1011
length = len(str(bin)) - 1
decimal = 0
a = 0
for i in str(bin):
    decimal += int(i) * (2 ** (length - a))
    
    a+=1
print(decimal)    