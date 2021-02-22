def generate_fibonacci(N):
    numbers=[0, 1]
    count=len(numbers)
    while count!=N:
        numbers.append(numbers[count-1]+numbers[count-2])
        count+=1
    return numbers
    
N=10
print (generate_fibonacci(N))
