class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        
    def insert(self, data):
        tmp = Node(data)
        
        if self.head is None:
            self.head = tmp
            self.last = tmp
            return
        
        while self.last.next!=None:
            self.last = self.last.next
        self.last.next = tmp
    
    def printList(self):
        curr = self.head
        while curr!=None:
            print (curr.data)
            curr = curr.next
    
def find_middle(List):
    curr1 ,curr2 = List.head, List.head
    
    while curr2.next!=None:
        curr1 = curr1.next
        if curr2.next.next:
            curr2 = curr2.next.next
            continue
        return curr1.data
    return curr1.data
        

List = LinkedList()
List.insert(1)
List.insert(2)
List.insert(3)
List.insert(4)
List.insert(5)

List.printList()
print ('-'*10)
print (find_middle(List))
