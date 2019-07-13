class Node:
    def __init__(self,val):
        self.info = val
        self.link = None

class SingleLinkedList:
    def __init__(self):
        self.start = None


list = SingleLinkedList()

def insert(val):
    if list.start == None:
        list.start = Node(val)
    else:
        temp = Node(val)
        temp.link = list.start
        list.start = temp

def traverseLinked():
    if list.start == None:
        print('linked list empty')
    else:
        p = list.start
        while p is not None:
            print(str(p.info) + ' ' ,end=' ')
            p = p.link

def deletAtBeg():
    p = list.start
    if p is None:
        print('list is empty')
        return
    list.start = list.start.link

def deletAtEnd():
    p = list.start
    if p is None:
        print('list is empty')
        return
    else:
        while p.link.link is not None:
            p = p.link
        p.link = None

def deletAtMid(val):
    p = list.start
    if p is None:
        print('list is empty')
        return
    elif p.info == val:
        list.start = p.link
        print('node deleted at first position')
    else:
        while p.link.info is not val:
            p = p.link
        if p.link.link is None:
            p.link = None
        else:
            p.link = p.link.link




n = 0
print('press 1 for insert at begg')
print('press 2 for traverse linked list')
print('press 3 for deletion at beg')
print('press 4 for deletion at end')
print('press 5 for deletion perticular node')



print('press 111 for exit')
while n is not 111:
    n = int(input("Press Number:-"))
    if n == 1:
        value = int(input('Enter Integer value:-'))
        insert(value)
        print('value ' + str(value) + ' inseted')
        continue

    elif n == 2:
        traverseLinked()
        print()
        continue

    elif n == 3:
        deletAtBeg()
        continue
    elif n == 4:
        deletAtEnd()
        continue
    elif n == 5:
        value = int(input('Enter value of node to delete'))
        deletAtMid(value)
        continue

    else:
        break



