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
    
    def traverse(self):
        curr = self.head
        while curr!=None:
            print (curr.data)
            curr = curr.next
    
def kth_node_from_end(List, k):
    ptr1 = List.head
    ptr2 = List.head
    while k!=0:
        ptr2 = ptr2.next
        k -= 1
    
    while ptr2!=None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    
    return ptr1.data

List = LinkedList()
List.insert(1)
List.insert(2)
List.insert(3)
List.insert(4)
List.insert(5)
List.insert(6)

List.traverse()
print ('-'*10)

k=4
print (kth_node_from_end(List, k))
