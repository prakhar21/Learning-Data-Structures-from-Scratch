def generate_combination(n, possible_digits):
    queue = []
    for digit in possible_digits:
        queue.append(digit)
    
    while len(queue)!=n:
        first = queue[0]
        queue.pop(0)

        for digit in possible_digits:
            queue.append(first+digit)
            
    return queue

if __name__ == '__main__':
    n = 7
    possible_digits = ['1', '7']
    print (generate_combination(n, possible_digits))
