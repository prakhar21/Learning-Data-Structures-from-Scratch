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

traversedlevel = 0
def right_most(root, level=1):
    global traversedlevel
    
    if root == None: return
    
    if traversedlevel < level:
        print (root.data)
        # print ("----"+str(maxlevel)+"----"+str(level)+"----")
        traversedlevel = level
        
    right_most(root.right, level+1)
    right_most(root.left, level+1)

#        10
#       /  \
#      8   11
#     / \    \
#    4   9    12
#     \        
#      5       

root = Node(10)
root.insert(8)
root.insert(9)
root.insert(4)
root.insert(5)
root.insert(11)
root.insert(12)
print (right_most(root))
