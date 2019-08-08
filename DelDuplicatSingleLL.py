class Node:
    def __init__(self,value):
        self.info = value
        self.link = None

class SingleLinked:
    def __init__(self):
        self.start = None


list = SingleLinked()

def insertAtEnd(value):  #insert element at end of linked list
    if list.start is None:
        list.start = Node(value)
    else:
        k = list.start
        while k.link is not None:
            k = k.link
        k.link = Node(value)
    
def traverse():    # to traverse the linked list
    k = list.start
    if list.start is None:
        print("list is empty")
    else:
        while k is not None:
            print(k.info,end=" ")
            k = k.link

def removeDuplicate():
    k = list.start
    while k is not None:
        s = k.info  #info of the current k node
        t = k
        while t is not None:   # we check from the current value of k
            if t.link is not None and s == t.link.info:  # check if t.link is not None because info part 
                t.link = t.link.link                     # has to be check otherwise return AttributeError:
            else:
                t = t.link
        k = k.link

        

    
p = ''' 
     press 1 to insert at end
     press 2 to traverse the list
     press 3 to remove all the duplicate element 
'''
print(p)

n = 0
while n is not 111:
    n = int(input("Press Number:-"))
    if n == 1:
        value = int(input('Enter Integer value:-'))
        insertAtEnd(value)
        print('value ' + str(value) + ' inseted')
    elif n == 2:
        traverse()
    elif n == 3:
        removeDuplicate()
    else:
        break


    