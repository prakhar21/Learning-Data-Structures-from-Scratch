class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, val):
        if self.data:
            if val < self.data:
                if self.left is not None:
                    self.left.insert(val)
                else:
                    self.left = Node(val)
            else:
                if self.right is not None:
                    self.right.insert(val)
                else:
                    self.right = Node(val)
        else:
            self.data = data
    
def postorder(root):
    if root != None:
        postorder(root.left)
        postorder(root.right)
        print (root.data)

root = Node(20)
root.insert(10)
root.insert(6)
root.insert(11)
root.insert(22)
root.insert(21)

postorder(root)
