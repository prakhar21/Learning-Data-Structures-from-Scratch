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
    
def find_value(root, val):
    if root!=None:
        if val > root.data:
            find_value(root.right, val)
        elif val < root.data:
            find_value(root.left, val)
        elif val==root.data:
            print ('Found!')
    else: print ('Not Found!')
    
root = Node(20)
root.insert(10)
root.insert(6)
root.insert(11)
root.insert(22)
root.insert(21)
find_value(root, 22)
