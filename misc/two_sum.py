def get_two_sum(data, target):
    tmp = dict()
    for idx, i in enumerate(data):
        if (target-i) in tmp:
            return tmp[target-i], idx
        else:
            tmp[i] = idx

data = [3, 2, 4, 1, 6, 2]
target = 10
print (get_two_sum(data, target))
