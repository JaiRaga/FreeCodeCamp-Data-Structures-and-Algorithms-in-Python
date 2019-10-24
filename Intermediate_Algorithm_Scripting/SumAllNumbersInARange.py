def sumAll(lis):
    lis.sort()
    sum = 0
    for i in range(lis[0], lis[1]+1):
        sum += i
    return sum


print(sumAll([1, 4]))
print(sumAll([10, 5]))
print(sumAll([8,7]))
