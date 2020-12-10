def count_distinct(sub_list):
    tmp_cnt = {}
    for element in sub_list:
        if element in tmp_cnt:
            tmp_cnt.pop(element)
        else:
            tmp_cnt[element] = True
    return len(tmp_cnt.keys())

def create_window(data, k):
    windows = []
    for idx in range(len(data)):
        tmp = data[idx:idx+k]
        if len(tmp)==k:
            windows.append(tmp)
    return windows
    
if __name__ == '__main__':
    results = []
    data = [1,2,1,3,4,2,3,2]
    k = 3
    windows = create_window(data, k)
    for window in windows:
        print ('Window: ' , window)
        print ('Distinct: ', count_distinct(window))
     
    
