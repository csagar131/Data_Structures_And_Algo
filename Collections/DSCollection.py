#---------QUEUE----------------         

from collections import deque 
queue = deque(["Ram", "Tarun", "Asif", "John"]) 
print(queue) 
queue.append("Akbar") 
print(queue) 
queue.append("Birbal") 
print(queue) 
print(queue.popleft())                  
print(queue.popleft())                  
print(queue) 

#################################################################
all(v is None for v in queue)    #return True if all element in list are None
