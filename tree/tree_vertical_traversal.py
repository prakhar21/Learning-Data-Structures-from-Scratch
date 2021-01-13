from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def vertical_traversal(root, hd, q):
    if root == None: return q
    
    if hd in q:
        q[hd].append(root.data)
    else:
        q[hd] = [root.data]
    
    vertical_traversal(root.left, hd-1, q)
    vertical_traversal(root.right, hd+1, q)
        
root = Node('a')
root.left = Node('b')
root.left.right = Node('e')
root.left.left = Node('d')
root.left.left.right = Node('l')
root.right = Node('c')
root.right.left = Node('f')
root.right.right = Node('g')

coll = {}
hd = 0
vertical_traversal(root, hd, coll)
for k,v in coll.items():
    print (k, v)
