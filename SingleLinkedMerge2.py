class Node:
    def __init__(self,val):
        self.info = val
        self.link = None

class SingleLinkedList:
    def __init__(self):
        self.start = None


list = SingleLinkedList()
list1 = SingleLinkedList()
list2 = SingleLinkedList()
p = list
p1 = list1
p2 = list2

def insertAtEnd(val,p):
    if p.start == None:
        p.start = Node(val)
    else:
        p = p.start
        while p.link is not None:
            p = p.link
        p.link = Node(val)

def traverseLinked(p):
    if p.start is  None:
        print('linked list empty')
    else:
        p = p.start
        while p is not None:
            print(str(p.info) + ' ' ,end=' ')
            p = p.link

# insert for first list
n1 = 0
print("enter value in first linked list")
while n1 is not 8:
    n1 = int(input("Enter n1:"))
    if n1 is 1:
        n = int(input("Enter value:"))
        insertAtEnd(n, list1)
    else:
        break
traverseLinked(list1)
n2 = 0
print("enter value in second linked list")
while n2 is not 8:
    n2 = int(input("Enter n2:"))
    if n2 is 1:
        n = int(input("Enter value:"))
        insertAtEnd(n, list2)
    else:
        break
traverseLinked(list2)









