class Node:
    def __init__(self,val):
        self.info = val
        self.link = None

class SingleLinkedList:
    def __init__(self):
        self.start = None


list = SingleLinkedList()

def insertAtEnd(val):
    if list.start == None:
        list.start = Node(val)
    else:
        p = list.start
        while p.link is not None:
            p = p.link
        p.link = Node(val)

def traverseLinked():
    if list.start == None:
        print('linked list empty')
    else:
        p = list.start
        while p is not None:
            print(str(p.info) + ' ' ,end=' ')
            p = p.link

def sort():
    p = list.start  # points to first node
    q = p.link      # points to node next to p
    while p.link is not None:
        while q is not None:
            if p.info > q.info:
                k = p.info
                p.info = q.info   #exchanging the info part if p.info > q.info
                q.info = k         # ie if previous node data is grater the nexts nodes
            q = q.link
        traverseLinked()
        print()
        p = p.link
        q = p.link

def bubbleSort():
    end = None
    k = list.start.link
    while end is not k:
        p = list.start
        q = p.link
        while p.link is not end:
            if p.info > q.info:  # throwing AttributeError at last need to review
                k = p.info
                p.info = q.info  # exchanging the info part if p.info > q.info
                q.info = k  # ie if previous node data is grater the nexts nodes
            q = q.link
            p = p.link
        traverseLinked()
        print()
        end = p
    print("final sorted list:")
    traverseLinked()




n = 0
print('press 1 for insert at end')
print('press 2 for traverse linked list')
print('press 3 for sort linked list')
print('press 4 for bubbles sort linked list')

print('press 111 for exit')

while n is not 111:
    n = int(input("Press Number:-"))
    if n == 1:
        value = int(input('Enter Integer value:-'))
        insertAtEnd(value)
        print('value ' + str(value) + ' inseted')
        continue

    elif n == 2:
        traverseLinked()
        print()

    elif n == 3:
        sort()
        continue
    elif n == 4:
        bubbleSort()
        continue
    else:
        break
