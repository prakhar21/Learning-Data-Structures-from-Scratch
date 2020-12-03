def previous_greater(a):
    stack, prev_grt = [], []
    
    for idx, i in enumerate(a):
        if idx==0:
            stack.append(i)
            prev_grt.append(-1)
        else:
            while len(stack)>0 and stack[-1] <= i: 
                stack.pop() 
            
            if len(stack)<=0:
                stack.append(i)
                prev_grt.append(-1)
            else:
                prev_grt.append(stack[-1])
                stack.append(i)
        
    return prev_grt

if __name__ == '__main__':
    print (previous_greater([15, 10, 18, 12, 4, 6, 2, 8]))
    //[-1, 15, -1, 18, 12, 12, 6, 12]
