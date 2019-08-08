class StackUnderflow(Exception):
    pass

class StackOverflow(Exception):
    pass

class StackEmpty(Exception):
    pass

class Node:
    def __init__(self,value):
        self.info = value
        self.link = None
    
class LinkedList:
    def __init__(self):
        self.top = None

list = LinkedList()

def push(value):
    if list.top is None:
        list.top = Node(value)
        print("value",value," is inserted")
    else:
        temp = Node(value)
        temp.link = list.top
        list.top = temp

def display():
    if list.top is None:
        raise StackEmpty("Stack is empty")
    else:
        k = list.top
        while k is not None:
            print(k.info,end=" ")
            k = k.link
    
def pop():
    if list.top is None:
        raise StackUnderflow("stack contains no element")
    else:
        print("poping element:",list.top.info)
        list.top = list.top.link 
    
p = '''

   enter 1 to push 
   enter 2 to pop
   enter 3 to show stack elements

'''

print(p)
choice = 99

while choice is not 0:
    choice = int(input("Enter your choice:-"))
    if choice == 1:
        n = int(input("Enter Number:"))
        push(n)
    elif choice  == 2:
        pop()
    elif choice == 3:
        display()
    else:
        break
    

        






