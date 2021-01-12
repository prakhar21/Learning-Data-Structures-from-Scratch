from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def count_leaf_nodes(root):
    if root==None: 
        return
    
    if root.left==None and root.right==None: 
        return 1
    else: 
        return count_leaf_nodes(root.left) + count_leaf_nodes(root.right) 

root = Node('a')
root.left = Node('c')
root.right = Node('b')
root.left.left = Node('d')
root.left.right = Node('e')
root.left.left.left = Node('g')
root.left.left.right = Node('f')

print (count_leaf_nodes(root))
