class Node:
    def __init__(self,data):
        self.info = data
        self.lchild = None
        self.rchild = None
    
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def preorder(self):
        self.preorderTraver(self.root)
        print()

    def preorderTraver(self,k):
        p = k
        if p is None:
            return
        print(p.info,end=" ")
        self.preorderTraver(p.lchild)
        self.preorderTraver(p.rchild)
    
    def insertTree(self,data=None):
        if self.root is None:
            r = Node(data)
            self.root = r
        else:
            p = self.root
            temp = Node(data)
            while True:
                if data < p.info:
                    while p.lchild is not None and data < p.info:
                        p = p.lchild
                    while p.rchild is not None and data > p.info:
                        p = p.rchild
                    if data > p.info:
                        p.rchild = temp
                        break
                    else:
                        p.lchild = temp
                        break

                else:
                    while p.lchild is not None and data < p.info:
                        p = p.lchild
                    while p.rchild is not None and data > p.info:
                        p = p.rchild
                    if data > p.info:
                        p.rchild = temp
                        break
                    else:
                        p.lchild = temp
                        break
        
        return self.root
    


s = """
0 for close
1 for insert continue
2 for preorder traverse
"""

b = BinaryTree()
n = 99


while n is not 0:
    n = int(input(s))
    if n == 1:
        data = int(input("ENter Number:"))
        b.insertTree(data)
    if n ==2:
        print("preorder traversing---->")
        b.preorder()
        break
    




