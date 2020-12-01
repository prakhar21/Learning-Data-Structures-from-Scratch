def remove_consecutive_duplicates(s):
    stack = list()
    if len(s):
        for idx, c in enumerate(s):
            if idx==0:
                stack.append(c)
            elif c!=stack[-1]:
                stack.append(c)
        return ''.join(stack)
        
    return 'Empty String'

if __name__ == '__main__':
    test = 'aaaaaabbaabcccccccd'
    result = remove_consecutive_duplicates(test)
    print (result)  //ababcd
    
