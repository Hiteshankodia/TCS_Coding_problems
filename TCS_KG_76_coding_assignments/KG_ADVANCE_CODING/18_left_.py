''' MS excel columuns have a pattern like A, B, C,..., Z,AA,AB...,AZ,BA..ZZ,AAA,AAB,.... In Other Words ,
columuns 1 named as 'A',columun 2 named as 'B', columun 27 as'AA'.
Given cl number , find the correspondingcl name. 
input: 26 Output:Z
input: 51 Output:AY
input: 52 Output:AZ
input: 80 Output:CB
input: 676 Output:YZ 
''' 
#algo- 1) do mod 26 if this is zero print z and result -1 and print the char 2) mod 26 is not zero print the corresponding char and divide karne pe jo result aa ra h uske hisab se digit

n = 48
a = ''
while (n>0):
    rem = n % 26 
    if (rem == 0):
        a = a+"Z"
        n = (n/26) -1 
    else:
        a = chr(int(rem-1)) + 'A'
        n = (n / 26)
        
print(a)
