class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
    
class LinkedList(Node):
    def __init__(self):
        self.head = None
        self.rear = None
    
    def enqueue(self, val):
        tmp = Node(val)
        self.rear.next = tmp
        self.rear = self.rear.next

    def dequeue(self):
        tmp = self.head
        self.head = self.head.next
        del tmp
        
    def traverse(self):
        ptr = self.head
        while ptr!=None:
            print (ptr.value)
            ptr = ptr.next

list = LinkedList()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
list.head = node1
list.rear = node1
node1.next = node2
list.rear = node2
node2.next = node3
list.rear = node3
node3.next = node4
list.rear = node4
list.traverse()
print ('---')
list.dequeue()
list.traverse()
print ('---')
list.enqueue(5)
list.enqueue(6)
list.dequeue()
list.traverse()
print ('---')
list.enqueue(7)
list.traverse()
