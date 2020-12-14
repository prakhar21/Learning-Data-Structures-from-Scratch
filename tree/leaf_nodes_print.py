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

def print_leaf_nodes(root):
    if root == None: 
        return
    
    if root.left==None and root.right==None:
        print (root.data)
        return
    
    print_leaf_nodes(root.left)
    print_leaf_nodes(root.right)

#        10
#       /  \
#      8   11
#     / \    \
#    4   9    12
#     \        \
#      5       15

root = Node(10)
root.insert(8)
root.insert(9)
root.insert(4)
root.insert(5)
root.insert(11)
root.insert(12)
root.insert(15)
print (print_leaf_nodes(root))
