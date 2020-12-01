 class Stack:
    def __init__(self, size):
        self.lst_stack = [None]*size
        self.top1=-1
        self.top2=size
    
    def check_overflow(self, stack):
        if stack==1:
            if self.top1==self.top2-1:
                return True
            else: return False
        else: 
            if self.top2==self.top1+1:
                return True
            else: return False
            
    def push1(self, value):
        overflow = self.check_overflow(1)
        if not overflow:
            self.top1=self.top1+1
            self.lst_stack[self.top1]=value
        else: 
            print ("Overflow for Stack 1")
            exit()
        
    def push2(self, value):
        overflow = self.check_overflow(2)
        if not overflow:
            self.top2 = self.top2-1
            self.lst_stack[self.top2]=value
        else: 
            print ("Overflow for Stack 2")
            exit()
        
    def pop1(self):
        if self.top1==-1:
            print ("Underflow for Stack 1")
            exit()
        self.lst_stack[self.top1]=None
        self.top1=self.top1-1
    
    def pop2(self):
        if self.top2==size-1:
            print ("Underflow for Stack 2")
            exit()
        self.lst_stack[self.top2]=None
        self.top2=self.top2+1
    
    def printStack(self):
        return self.lst_stack

if __name__=="__main__":
    size=6
    stack = Stack(size)
    stack.push1(1)
    stack.pop1()
    stack.push2(5)
    stack.push2(3)
    stack.push2(2)
    stack.pop2()
    stack.push1(10)
    stack.push1(14)
    stack.push1(15)
    stack.push1(17)
    # stack.push1(12) // overflow
    print (stack.printStack())
    
