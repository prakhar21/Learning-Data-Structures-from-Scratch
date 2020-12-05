class queue:
    def __init__(self):
        self.lst_queue = []
    
    def enqueue(self, data):
        self.lst_queue.append(data)
    
    def dequeue(self):
        if self.size()==0:
            return -1
        else:
            self.lst_queue.pop(0)
    
    def size(self):
        return len(self.lst_queue)
    
    def isEmpty(self):
        if len(self.lst_queue): return False
        else: return True
    
    def getFirst(self):
        return self.lst_queue[0]
    
    def getRear(self):
        return self.lst_queue[-1]
    
    def traverse(self):
        for i in self.lst_queue:
            print (i)

class stack(queue):
    def __init__(self):
        self.q1 = queue()
        self.q2 = queue()
    
    def push(self, data):
        while not self.q1.isEmpty():
            tmp = self.q1.getFirst()
            self.q1.dequeue()
            self.q2.enqueue(tmp)
        self.q1.enqueue(data)
        while not self.q2.isEmpty():
            tmp = self.q2.getFirst()
            self.q2.dequeue()
            self.q1.enqueue(tmp)

    def pop(self):
        self.q1.dequeue()
        
    def printStack(self):
        self.q1.traverse()


s = stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.printStack()
print ('---')
s.pop()
s.printStack()
print ('---')
s.push(5)
s.printStack()
print ('---')
s.pop()
s.printStack()
