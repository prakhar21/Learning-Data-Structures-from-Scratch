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

def size(root):
    if root == None:
        return 0
    return size(root.left) + size(root.right) + 1

#        10
#       /  \
#      8   11
#     / \    \
#    4   9    12
#   /          \
#  3           13

root = Node(10)
root.insert(8)
root.insert(9)
root.insert(4)
root.insert(3)
root.insert(11)
root.insert(12)
root.insert(13)
print (size(root)) #8
