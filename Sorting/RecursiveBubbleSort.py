
import random
lst = []
for i in range(10):
    lst.append(random.randint(1,10))
print(lst)
print("------------------")
def recBubble(lst,n):
    if len(lst) == 1:
        return 
    else:
        try:
            for i in range(0,n):
                if lst[i] > lst[i+1]:
                    lst[i],lst[i+1] = lst[i+1], lst[i]
                recBubble(lst,n-1)
        except IndexError:
            pass
recBubble(lst,len(lst))
print(lst)