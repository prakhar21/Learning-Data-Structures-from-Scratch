def get_span(a):
    stack, span = [], []
    
    for idx, i in enumerate(a):
        if idx==0:
            stack.append(0)
            span.append(1)
        else:
            while len(stack)>0 and a[stack[-1]] <= i: 
                stack.pop() 
            
            if len(stack)<=0:
                span.append(idx+1)
                stack.append(idx)
            else:
                span.append(idx-stack[-1])
                stack.append(idx)
    return span

if __name__ == '__main__':
    print (get_span([100, 80, 60, 70, 60, 75, 85]))
    //1, 1, 1, 2, 1, 4, 6
