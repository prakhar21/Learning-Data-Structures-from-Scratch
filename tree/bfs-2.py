from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def bfs(root):
    queue = deque([])
    if root==None: return
    queue.append(root)
    queue.append(None)
    while len(queue)!=0:
        current = queue.popleft()
        if current==None:
            print ('-')
            queue.append(None)
        else: 
            print (current.data)
            if current.left!=None: queue.append(current.left)
            if current.right!=None: queue.append(current.right)
        
    

root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.left.right = Node('e')
root.left.left.left = Node('h')
root.left.left.right = Node('i')

root.right = Node('c')
root.right.left = Node('f')
root.right.right = Node('g')


bfs(root)
