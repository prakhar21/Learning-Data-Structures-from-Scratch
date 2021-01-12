from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def dfs(root):
    if root==None: return
    print (root.data)
    dfs(root.left)
    dfs(root.right)

root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.left.right = Node('e')
root.left.left.left = Node('h')
root.left.left.right = Node('i')

root.right = Node('c')
root.right.left = Node('f')
root.right.right = Node('g')

dfs(root)
