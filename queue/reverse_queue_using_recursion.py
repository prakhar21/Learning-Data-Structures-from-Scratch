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

def reverse(q):
    if q.isEmpty(): return q
    
    tmp = q.getFirst()
    q.dequeue()
    reverse(q)
    q.enqueue(tmp)
    

q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
q.traverse()
print ('---')
reverse(q)
q.traverse()
