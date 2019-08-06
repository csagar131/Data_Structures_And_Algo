import random
lst = []
for i in range(10):
    lst.append(random.randint(1,10))

print("list before sorting")
print(lst)
print("---------------------")
for i in range(len(lst)):
    for j in range(0,len(lst)-1):
        if lst[j] >= lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]

    print(lst)
print("list after bubble sort")
print(lst)

    