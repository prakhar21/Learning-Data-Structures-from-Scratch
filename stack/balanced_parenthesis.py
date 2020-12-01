class Stack:
    def __init__(self):
        self.lst_stack = list()
    
    def push(self, value):
        self.lst_stack.append(value)
    
    def pop(self):
        self.lst_stack.pop()
    
    def peek(self):
        return self.lst_stack[-1]
    
    def isEmpty(self):
        if len(self.lst_stack)==0: return True
        else: return False
    
    def size(self):
        return len(self.lst_stack)
        
def check_for_balanced_paranthesis(cases):
    results = []
    for case in cases:
        not_balanced=False
        for char in case:
            if char in ["{", "[", "("]:
                stack.push(char)
            else:
                if stack.isEmpty():
                    not_balanced=True
                    results.append("Not Balanced")
                    break
                
                if (stack.peek()=="[" and char=="]") or (stack.peek()=="{" and char=="}") or (stack.peek()=="(" and char==")"):
                    stack.pop()
                else:
                    not_balanced=True
                    results.append("Not Balanced")
                    break
                
        if not not_balanced:
            results.append("Balanced")
            
    return results

if __name__=="__main__":
    test = ["([])", "}{", "[(()){}]", "())", "([)]", "{[()]}", "{}[]()[{(})]"]
    stack = Stack()
    results = check_for_balanced_paranthesis(test)
    for i,j in zip(test, results):
        print (i, '->', j)

"""
([]) -> Balanced
}{ -> Not Balanced
[(()){}] -> Balanced
()) -> Not Balanced
([)] -> Not Balanced
{[()]} -> Balanced
{}[]()[{(})] -> Not Balanced
"""
