class Node:
    def __init__(self,val):
        self.info = val
        self.link = None

class SingleLinkedList:
    def __init__(self):
        self.start = None


list1 = SingleLinkedList()
list2 = SingleLinkedList()



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

p1 = list1
p2 = list2
startm = None  # where the merged list first node points to
pm = None      # this will used to change address at specified point of merged list

# initially startm will be None so
if startm is None:
    if p1.info <= p2.info:
        startm = p1
        pm = p1
        p1 = p1.link
    else:
        startm = p2
        pm = p2
        p2 = p2.link

# now our merged list has come into picture we will continue adding

while p1 is not None or p2 is not None:
    if p1.info <= p2.info:
        pm.link = p1
        pm = p1
        p1 = p1.link
    else:
        pm.link = p2
        pm = p2
        p2 = p2.link

if p1 is None:
    p1.link = p2
else:
    p2.link = p1


traverseLinked(startm)




