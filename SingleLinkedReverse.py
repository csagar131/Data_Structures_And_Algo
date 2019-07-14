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

def reverse():
    p = None           # p maintain the address of previous node
    q = list.start
    while q is not None:
        r = q.link        # maintain the address of next node
        q.link = p
        p = q
        q = r            # maintain the address of current node
    list.start = p


n = 0
print('press 1 for insert at begg')
print('press 2 for traverse linked list')
print('press 3 for reverse the list')
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
        reverse()
        continue
    else:
        break



