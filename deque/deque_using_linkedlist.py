class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.val = data
        self.next = next
        self.prev = prev

class Deque(Node):
    def __init__(self):
        self.head = None
        self.size = 0
        self.rear = None
    
    def insertFront(self, val):
        tmp = Node(data=val)
        tmp.next = self.head
        tmp.prev = None
        
        if self.head is not None:
            self.head.prev = tmp
            self.head = tmp
        else:
            self.rear = tmp
            self.head = tmp
        self.size += 1
    
    def getFront(self):
        return self.head.val
    
    def deleteFront(self):
        tmp = self.head.val
        self.head = self.head.next
        self.head.prev = None
        del tmp
        
    def insertRear(self, val):
        tmp = Node(data=val)
        tmp.next = None
        
        if self.rear is not None:
            self.rear.next = tmp
            tmp.prev = self.rear
            self.rear = tmp
        else:
            tmp.prev = self.rear
            self.rear = tmp
        self.size += 1
    
    def deleteRear(self):
        tmp = self.rear.val
        self.rear = self.rear.prev
        self.rear.next = None
        del tmp
        
    def getRear(self):
        return self.rear.val
    
    def getSize(self):
        return self.size
        
    def traverse(self):
        tmp = self.head
        while tmp!=None:
            print (tmp.val)
            tmp = tmp.next

deque = Deque()
deque.insertFront(1)
deque.insertFront(2)
deque.insertFront(3)
deque.insertFront(4)
print (deque.traverse())
print ()
print ('Front - ' + str(deque.getFront()))
print ('Size - ' + str(deque.getSize()))
print ('Last - ' + str(deque.getRear()))
deque.insertRear(10)
print ()
print (deque.traverse())
print ()
print ('Last - ' + str(deque.getRear()))
print ('Front - ' + str(deque.getFront()))
print ()
deque.deleteRear()
deque.deleteFront()   
print (deque.traverse())
print ()
print ('Last - ' + str(deque.getRear()))
print ('Front - ' + str(deque.getFront()))

