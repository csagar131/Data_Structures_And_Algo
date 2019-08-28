def checkPrime(num):
    n = num
    rev = 0
    while n > 0:
        a = n % 10
        rev = rev*10+a
        n = n//10
    if num == rev:
        return True
    return False

def largestPrime(lst):
    mx = 0
    for i in lst:
        if checkPrime(i):
            c = len(str(i))
            if c >= mx:
                mx = c
                num = i
    print(f'largest prime {num} with {mx} max')
    print()

print("enter list element")
n = [1, 121, 12321, 11, 123456, 34567876543]
largestPrime(n)



