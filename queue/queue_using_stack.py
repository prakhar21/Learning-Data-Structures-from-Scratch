class stack:
    def __init__(self):
        self.lst_stack = []
    
    def push(self, val):
        self.lst_stack.append(val)
    
    def peek(self):
        return self.lst_stack[-1]
    
    def size(self):
        return len(self.lst_stack)
    
    def pop(self):
        if self.size():
            self.lst_stack.pop()
        else:
            return -1

class queue(stack):
    def __init__(self):
        self.s1 = stack()
        self.s2 = stack()
    
    def enqueue(self, val):
        self.s1.push(val)
    
    def dequeue(self):
        if self.s2.size():
            self.s2.pop()
        else:
            while self.s1.size():
                top = self.s1.peek()
                self.s1.pop()
                self.s2.push(top)
            self.s2.pop()
    
    def traverse(self):
        return self.s1.lst_stack
    
q = queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
