from collections import deque

class Node:
    def __init__(self,data):
        self.info = data
        self.lchild = None
        self.rchild = None
    
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def preorder(self):
        self.preorderTravers(self.root)
        print()

    def inorder(self):
        self.inorderTravers(self.root)
        print()
    
    def postorder(self):
        self.postorderTravers(self.root)
        print()

    def leveorder(self):
        self.levelorderTravers(self.root)
        print()
    
    def levelorderTravers(self,k):
        p = k
        queue = deque([p])
        if p is None:
            return 
        else:
            while p is not None or len(queue) is not 0:
                flag = all(v is None for v in queue)
                if queue[0] is not None:
                    print(queue[0].info,end=" ")
                else:
                    if not flag:
                        queue.popleft()
                        continue
                    else:
                        break
                p=queue.popleft()
                queue.append(p.lchild)
                queue.append(p.rchild)




    
    def postorderTravers(self,k):
        p = k
        if p is None:
            return
        self.postorderTravers(p.lchild)
        self.postorderTravers(p.rchild)
        print(p.info,end=" ")

    def inorderTravers(self,k):
        p = k
        if p is None:
            return
        self.inorderTravers(p.lchild)
        print(p.info,end=" ")
        self.inorderTravers(p.rchild)

    def preorderTravers(self,k):
        p = k
        if p is None:
            return
        print(p.info,end=" ")
        self.preorderTravers(p.lchild)
        self.preorderTravers(p.rchild)
    
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
3 for inorder traverse
4 for postorder traverse
5 for level order traverse
"""

b = BinaryTree()
n = 99


while n is not 0:
    n = int(input(s))
    if n == 1:
        data = int(input("ENter Number:"))
        b.insertTree(data)
    elif n ==2:
        print("preorder traversing---->")
        b.preorder()
        break
    elif n == 3:
        print("inorder traversing---->")
        b.inorder()
        break
    elif n == 4:
        print("postorder traversing--->")
        b.postorder()
        break
    elif n == 5:
        print("level order traversal--->")
        b.leveorder()
        break
    else:
        continue

    




