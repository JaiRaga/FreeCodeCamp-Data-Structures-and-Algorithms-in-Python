def getIndexToIns(lis, num):
    if len(lis) == 0:
        return 0
    for i in range(len(lis)):
        if lis[i] >= num:
            return i
        elif i == len(lis)-1:
            return len(lis)




print(getIndexToIns([10, 20, 30, 40, 50], 35))
print(getIndexToIns([10, 20, 30, 40, 50], 30))
print(getIndexToIns([3, 10, 5], 3))
print(getIndexToIns([2, 5, 10], 15))
print(getIndexToIns([], 1))