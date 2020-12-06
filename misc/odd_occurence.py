def findOddOccurence(data):
    odd_collection = dict()
    for i in data:
        if i in odd_collection:
            odd_collection.pop(i)
        else:
            odd_collection[i] = True
    return odd_collection
            
    
if __name__ == '__main__':
    data = [1,2,5,3,4,5,4,3,6,2,1]
    print (findOddOccurence(data))
