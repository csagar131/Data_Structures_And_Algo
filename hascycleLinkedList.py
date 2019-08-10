"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    k = head
    lst = []
    r = False
    while k is not None:
        if k in lst:
            r = True
            break
        else:
            lst.append(k)
            k = k.next
    return r
        
