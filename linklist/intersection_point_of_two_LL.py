class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        curr = self.head
        while curr!=None:
            print (curr.data)
            curr = curr.next
    
    def insert(self, data):
        tmp = Node(data)
        tmp.next = self.head
        self.head = tmp
    
    def length(self):
        L=0
        curr = self.head
        while curr!=None:
            curr = curr.next
            L += 1
        return L

def intersection_element(l1, l2, diff):
    curr1 = l1.head
    while diff:
        curr1 = curr1.next
        diff = diff-1
    
    curr2 = l2.head
    while curr1!=None:
        curr1 = curr1.next
        curr2 = curr2.next
        if curr1.data == curr2.data:
            return curr1.data
    return 'not found'

List1 = LinkedList()
List1.insert(1)
List1.insert(3)
List1.insert(0)
List1.insert(4)
List1.insert(5)

List2 = LinkedList()
List2.insert(1)
List2.insert(3)
List2.insert(-2)
List2.insert(-1)

print (intersection_element(List1, List2, List1.length()-List2.length()))
