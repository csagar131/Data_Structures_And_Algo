class Node:
    def __init__(self,value):
        self.info = value
        self.link = None

class SingleLinked:
    def __init__(self):
        self.start = None


list = SingleLinked()

def insertAtBeg(value):
    if list.start == None:
        list.start = Node(value)
        list.start.link = None
    else:
        lnk = list.start
        list.start = Node(value)
        list.start.link =lnk

def traverseLinked():
    p = list.start
    while p is not None:
        print(str(p.info) + ' ' ,end=' ')
        p = p.link
    return 3


print('press 1 for insert at begg')
print('press 2 for traverse linked list')
print('press 3 for exit')
n = int(input("Press Number:-"))
while True:
    print('press 1 for insert at begg')
    print('press 2 for traverse linked list')
    print('press 3 for exit')

    if n == 1:
        value = int(input('Enter Integer value:-'))
        insertAtBeg(value)
        print('value ' + str(value) + ' inseted')
        n = int(input("Press Number:-"))
    elif n == 2:
        n = traverseLinked()
        print()
    else:
        break