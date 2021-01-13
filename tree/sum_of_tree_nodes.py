class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sum_tree_nodes(root):
    if root==None: return 0
    return root.data + sum_tree_nodes(root.left) + sum_tree_nodes(root.right)

root = Node(10)
root.left = Node(5)
root.right = Node(12)

root.left.right = Node(7)
root.right.right = Node(15)

print (sum_tree_nodes(root))
