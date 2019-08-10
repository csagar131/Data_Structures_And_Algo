class Node:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
    
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insertTree(self,data):
        if self.root is None:
            r = Node(data)
            root = r
        else:


