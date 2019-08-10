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

p1 = list1.start
p2 = list2.start
p = list               # for easy identify purpose

# merging two list
while p1.link is not None or p2.link is not None:
    if p.start is None:
        if p1.info <= p2.info:
            insertAtEnd(p1.info,p)
            p1 = p1.link
        else:
            insertAtEnd(p2.info, p)
            p2 = p2.link
    else:
        if p1.info <= p2.info:
            insertAtEnd(p1.info, p)
            p1 = p1.link
        else:
            insertAtEnd(p2.info, p)
            p2 = p2.link

# when list1 pointer points to None
while p2 is not None:
    insertAtEnd(p2.info,p)
    p2 = p2.link


while p1 is not None:
    insertAtEnd(p1.info,p)
    p1 = p1.link

print("-----------------------------")
traverseLinked(list)












