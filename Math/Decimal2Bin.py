n = int(input("Enter N:"))

num = ''
while n > 0:
    k = n % 2        # to convert to any other formate divide by that base
    num = num + str(k)
    n = n // 2

m = ''
lst = list(num)
lst.reverse()
m  = m.join(lst)
print(m)
print(type(m)) # type is string
