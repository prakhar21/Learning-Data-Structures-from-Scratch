def insert_at_last(stack, tmp):
    if len(stack)<=0:
        stack.append(tmp)
        return stack
    
    temp = stack[-1]
    stack.pop()
    insert_at_last(stack, tmp)
    stack.append(temp)
    
def reverse_stack(stack):
    if len(stack)<=0:
        return stack
    
    tmp=stack[-1]
    stack.pop()
    
    reverse_stack(stack)
    insert_at_last(stack, tmp)
    return stack


if __name__ == '__main__':
    print (reverse_stack([1,2,3,4,5]))
    //5,4,3,2,1
