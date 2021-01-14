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
        if self.head == None:
            self.head = tmp
            self.tail = tmp
            return
        
        while self.tail.next != None:
            self.tail = self.tail.next
        self.tail.next = tmp
    
    def printList(self):
        curr = self.head
        while curr:
            print (curr.data)
            curr = curr.next

coll = {}
def deduplicate_unsorted(List):
    global coll
    curr = List.head.next
    prev = List.head
    coll[prev.data] = 1
    while curr!=None:
        if curr.data not in coll:
            coll[curr.data] = 1
            prev = prev.next
            curr = curr.next
        else:
            prev.next = curr.next
            temp = curr
            del temp
            curr = curr.next

List = LinkedList()
List.insert(1)
List.insert(4)
List.insert(3)
List.insert(1)
List.insert(4)
List.insert(5)
List.printList()
print ('-'*10)
deduplicate_unsorted(List)
List.printList()        
            
            
