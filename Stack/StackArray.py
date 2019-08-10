class EmptyStackError(Exception):
    pass

class Stack:
    def __init__(self):
        self.lst = []
    
    def isEmpty(self):
        if len(self.lst) == 0:
            return True
    
    def push(self,item):
        self.lst.append(item)
    
    def pop(self):
        if self.isEmpty():
            raise EmptyStackError("Stack is empty")
        self.lst.pop()
        
    def peek(self):
        if self.isEmpty():
            raise EmptyStackError("Stack is empty")
        return self.lst[-1]
        
    def display(self):
        print(self.lst)

stack = Stack()

p = '''
     enter 1 to push
     enter 2 to pop
     enter 3 to check if stack is empty
     enter 4 to display the stack element
     enter 5 to check element at top
     enter 0 to close this operation
'''

print(p)
choice = 99
while choice is not 0:
    choice = int(input("enter your choice:- "))
    if choice == 1:
        n = int(input("enter number:-"))
        stack.push(n)
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        if stack.isEmpty():
            print("yes its empty")
        else:
            print("its not")
    elif choice == 4:
        stack.display()
    elif choice == 5:
        x=stack.peek()
        print("element at top is:",x)
    else:
        break



        