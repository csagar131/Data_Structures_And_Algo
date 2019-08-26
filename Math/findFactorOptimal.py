import math

n = int(input("Enter N:"))
lst= []
for i in range(1,int(math.sqrt(n)+1)):
    if n % i == 0:
        lst.append(i)
        if i != int(math.sqrt(n)):
            lst.append(n//i)

lst.sort()
print(lst)

'''
time complexity will O(sqrt(n))  better than O(n)  

'''