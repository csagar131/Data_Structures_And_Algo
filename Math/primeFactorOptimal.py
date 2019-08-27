import math
n = int(input("Enter N:"))


for i in range(2,int(math.sqrt(n))):
    if n % i == 0:
        c = 0
        while n % i == 0:
            n = n // i
            c+=1
        print(int(math.pow(i,c)))
        print(i,c)

if  n != 1:
    print(math.pow(n,1))
    print(n,1)



