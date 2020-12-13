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

def nodes_at_k_distance(root, k, dist=0):
    if root == None:
        return
    
    if k == dist:
        print (root.data)
        dist -= 1
        return 
    
    if root != None:
        nodes_at_k_distance(root.left, k, dist+1)
        nodes_at_k_distance(root.right, k, dist+1)

#       10
#       /  \
#      8   11
#     / \    \
#    4   9    12
#   /          \
#  3           13
 

k=2  #4, 9, 12
root = Node(10)
root.insert(8)
root.insert(9)
root.insert(4)
root.insert(3)
root.insert(11)
root.insert(12)
root.insert(13)
print (nodes_at_k_distance(root, k))
