import math

class Stack:
    def __init__(self):
        self.lst_stack = list()
    
    def push(self, value):
        self.lst_stack.append(value)
    
    def pop(self):
        self.lst_stack.pop()
    
    def isEmpty(self):
        if len(self.lst_stack): return False
        else: return True

def deleteMiddle(stack, size, idx=1):
    if stack.isEmpty():
        return
    
    tmp = stack.lst_stack[-1]
    stack.pop()
    
    deleteMiddle(stack, size, idx+1)
    
    if math.ceil(size/2.0) != idx:
        stack.push(tmp)
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

deleteMiddle(stack, len(stack.lst_stack))

print (stack.lst_stack)
