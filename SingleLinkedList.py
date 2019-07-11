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
    if list.start == None:
        print('linked list empty')
    else:
        p = list.start
        while p is not None:
            print(str(p.info) + ' ' ,end=' ')
            p = p.link


def countNodes():
    p = list.start
    count = 0
    while p is not None:
        count = count + 1
        p = p.link
    return count

def findInfo(x):
    if list.start == None:
        print('linked list empty')
    else:
        p = list.start
        pos = 1
        while p is not None:
            if p.info == x:
                print('element ' + str(x) + ' found at position:' + str(pos))
                break
            else:
                p = p.link
                pos = pos + 1



n = 0
print('press 1 for insert at begg')
print('press 2 for traverse linked list')
print('press 3 for counting the nodes')
print('press 4 to find element in the list')
print('press 111 for exit')
while n is not 111:

    n = int(input("Press Number:-"))

    if n == 1:
        value = int(input('Enter Integer value:-'))
        insertAtBeg(value)
        print('value ' + str(value) + ' inseted')
    elif n == 2:
        traverseLinked()
        print()
        continue
    elif n == 3:
        count = countNodes()
        print('no of nodes in list is=' + str(count))
        continue
    elif n == 4:
        num = int(input('Enter no. to be found:-'))
        findInfo(num)
        continue
    else:
        break