import random
lst = []
for i in range(10):
    lst.append(random.randint(1,10))
print("Before sorting")
print(lst)

for i in range(1,len(lst)):
    key = lst[i]
    j = i

    while j>0 and lst[j-1] > key:
        lst[j]  = lst[j-1]
        j = j -1
    lst[j] = key

print("after sorting")
print(lst) 

'''
Worst Case Time Complexity [ Big-O ]: O(n2)
Best Case Time Complexity [Big-omega]: O(n)
Average Time Complexity [Big-theta]: O(n2)
'''