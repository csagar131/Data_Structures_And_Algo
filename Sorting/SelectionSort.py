import random
lst = []
for i in range(10):
    lst.append(random.randint(1,10))
print("Before sorting")
print(lst)
for i in range(len(lst)-1):
    minind = i 
    for j in range(i+1,len(lst)):
        if  lst[j] < lst[minind]:
            minind = j
    lst[i],lst[minind] = lst[minind],lst[i]
print("after sorting")
print(lst) 
