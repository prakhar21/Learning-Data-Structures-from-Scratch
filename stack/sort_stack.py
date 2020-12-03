def sort_stack(stack):
    stack1, stack2 = stack, []
    
    for i in range(len(stack1)-1, -1, -1):
        tmp = stack1[i]
        stack1.pop()
        
        if len(stack2)<=0:
            stack2.append(tmp)
        else:
            popped=0
            while stack2[-1] <= tmp:
                stack1.append(stack2[-1])
                stack2.pop()
                popped+=1
                if len(stack2)==0:
                    break

            stack2.append(tmp)
            
            for i in range(popped):
                stack2.append(stack1[-1])
                stack1.pop()
    return stack2

if __name__ == '__main__':
    print (sort_stack([10, 12, 7, 1, 100]))
    
    
