def next_greater_element(arr):
    stack, nxt_grt = [], []
    
    for i in range(len(arr)-1, -1, -1):
        if i==len(arr)-1:
            stack.append(arr[i])
            nxt_grt.append(-1)
        else:
            while len(stack)>0 and arr[i]>=stack[-1]:
                stack.pop()
            
            if len(stack)<=0:
                nxt_grt.append(-1)
                stack.append(arr[i])
            else:
                nxt_grt.append(stack[-1])
                stack.append(arr[i])
            
    return nxt_grt[::-1]

if __name__ == "__main__":
    print (next_greater_element([1 3 2 4]))
    //[3 4 4 -1]
    
