class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, data):
        tmp = Node(data)
        if self.head==None:
            self.head = tmp
            self.tail = tmp
            return
        
        while self.tail.next!=None:
            self.tail = self.tail.next
        self.tail.next = tmp
    
    def printList(self):
        curr = self.head
        while curr!=None:
            print (curr.data)
            curr = curr.next

def deduplicate_sorted(List):
    curr = List.head.next
    prev = List.head
    while curr!=None:
        if prev.data==curr.data:
            curr = curr.next
            if not curr:
                prev.next = None
                return
        else:
            prev.next = curr
            prev = curr
            curr = curr.next

List = LinkedList()
List.insert(1)
List.insert(2)
List.insert(2)
List.insert(3)
List.insert(3)
List.insert(4)
deduplicate_sorted(List)
List.printList()
