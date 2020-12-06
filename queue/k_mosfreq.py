def findTopK(data, k):
    count_store = {}
    for i in data:
        if i in count_store:
            count_store[i] += 1
        else:
            count_store[i] = 1
    
    count_idx = []
    for _k,_v in count_store.items():
        try:
            count_idx[_v-1].append(_k)
        except:
            tmp = []
            tmp.append(_k)
            count_idx.insert(_v-1, tmp)
    
    final = []
    c = 0
    for i in count_idx[::-1]:
        for j in i:
            c += 1
            final.append(j)
            if c == k:
                return final
    
if __name__ == '__main__':
    k = 3
    data = [3, 1, 1, 4, 5, 2, 6, 7, 7, 7, 8, 9, 9, 9]
    print (findTopK(data, k))
