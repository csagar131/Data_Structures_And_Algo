def gcd(a,b):
    if b == 0:
        print(f'gcd is {a}')
    else:
        gcd(b,a%b)
    

a = int(input("Enter Divisor:"))
b = int(input("Enter Divident"))

gcd(a,b)