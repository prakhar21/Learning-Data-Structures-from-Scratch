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

def height(root):
    if root!=None:
        return max(height(root.left), height(root.right))+1
    else: return 0

root = Node(10)
root.insert(8)
root.insert(9)
root.insert(4)
root.insert(3)
root.insert(11)
root.insert(12)
root.insert(13)
root.insert(14)
print (height(root))
