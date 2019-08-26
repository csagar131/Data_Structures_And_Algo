import math
n = int(input("ENter N:"))
lst = [1]*(n+1)
print(lst)

lst[0] = 0
lst[1] = 0

for i in range(2,int(math.sqrt(n))+1):
    if lst[i] == 1:
        j = 2
        while i*j <=n:
            lst[i*j] = 0   # all the multiples of prime  are set to zero whilch is non prime
            j+=1

print(lst)
for i,j in enumerate(lst):
    if j == 1:
        print(i)

'''
time complexity will O(n*loglog(n))

'''
