class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        tmp = Node(data)
        tmp.next = self.head
        self.head = tmp
    
    def reverse(self):
        curr = self.head
        prev = None
        while curr!=None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev
    
    def printList(self):
        curr = self.head
        while curr!=None:
            print (curr.data)
            curr = curr.next

List = LinkedList()
List.insert(1)
List.insert(2)
List.insert(3)
List.insert(4)
List.printList()
print ('-'*10)
List.reverse()
List.printList()
