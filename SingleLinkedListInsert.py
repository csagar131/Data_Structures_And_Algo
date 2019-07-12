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
        #list.start.link = None
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

def refLastNode():
    p = list.start
    while p.link is not None:
        p = p.link
    print('last node contains value ' + str(p.info) + ' and address ' + str(p))


def refSecondLastNode():
    p = list.start
    while p.link.link is not None:
        p = p.link
    print('second last node contains value ' + str(p.info) + ' and address ' + str(p))

def refPredInfo(x):
    p = list.start
    if p.info == x:
        print('this is the first node with info ' + str(p.info))
    else:
        while p.link is not None:
            if p.link.info is x:
                print('predecessor of give info is ' + str(p.info))
                break
            else:
                p = p.link
        else:
            print('element not listed in the list')

def refNodeAtPertPos(pos):
    p =list.start
    count = 1
    if pos == count:
        print('at position ' + str(pos) + '  info is ' + str(p.info))
    else:
        while count is not pos and p.link is not None:
            count = count + 1
            p = p.link
            if count is pos:
                print('element found at position ' + str(pos) + ' with info ' + str(p.info))
                break

def insertAtEnd(val):
    if list.start == None:
        list.start = Node(val)
    else:
        p = list.start
        while p.link is not None:
            p = p.link
        p.link = Node(val)


def insertBetNodes(val,n):
    count = 1
    p = list.start
    if p is None:
        print('list is empty')
    elif p.link is None:
        print('list contain 1 item')
        p.link = Node(val)
    else:
        while count < n:
            p = p.link
            count = count + 1
        addr = p.link
        p.link = Node(val)
        p.link.link = addr






n = 0
print('press 1 for insert at begg')
print('press 2 for traverse linked list')
print('press 3 for counting the nodes')
print('press 4 to find element in the list')
print('press 5 to find info about last node')
print('press 6 to find info about last node')
print('press 7 to find predecessor of given info node')
print('press 8 to find ref of perticular position')
print('press 9 to insert at end')
print('press 10 to insert after no. of nodes')

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
    elif n == 5:
        refLastNode()
        continue
    elif n == 6:
        refSecondLastNode()
        continue
    elif n == 7:
        num = int(input('Enter no. to whose prede be found:-'))
        refPredInfo(num)
        continue
    elif n == 8:
        pos = int(input('Enter the position to be found:-'))
        refNodeAtPertPos(pos)
        continue
    elif n == 9:
        value = int(input('Enter Integer value:-'))
        insertAtEnd(value)
        print('value ' + str(value) + ' inseted')

    elif n == 10:
        val  = int(input('Enter Integer value:'))
        n = int(input('Enter after how many nodes:'))
        insertBetNodes(val, n)
        print('value ' + str(val) + ' inseted')
        continue
    else:
        break