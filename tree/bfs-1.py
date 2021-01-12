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
    while len(queue)!=0:
        current = queue.popleft()
        print (current.data)
        if current.left!=None:
            queue.append(current.left)
        if current.right!=None:
            queue.append(current.right)

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(20)

bfs(root)

#10, 5, 15, 3, 7, 20
