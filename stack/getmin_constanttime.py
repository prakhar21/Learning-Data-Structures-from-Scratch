class Stack:
    def __init__(self):
        self.lst_stack = list()
        self.min_stack = list()
    
    def push(self, value):
        self.lst_stack.append(value)
        if len(self.min_stack)==0:
            self.min_stack.append(value)
        else:
            if self.min_stack[-1] <= value:
                self.min_stack.append(self.min_stack[-1])
            else: self.min_stack.append(value)
    
    def pop(self):
        self.lst_stack.pop()
        self.min_stack.pop()
    
    def peek(self):
        return self.lst_stack[-1]
    
    def isEmpty(self):
        if len(self.lst_stack)==0: return True
        else: return False
    
    def size(self):
        return len(self.lst_stack)
    
    def getMin(self):
        return self.min_stack[-1]

stack = Stack()
stack.push(25)
stack.push(92)
stack.push(9)
stack.pop()
stack.push(1)
stack.pop()
print (stack.getMin())
print (stack.lst_stack)
print (stack.min_stack)
