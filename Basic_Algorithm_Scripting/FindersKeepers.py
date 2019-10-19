def findElement(lis, func):
    num = None
    for i in lis:
        if func(i):
            num = i
            return num
    return num

def methodToCall(num):
    if num % 2 == 0:
        return True
    return False

print(findElement([1, 3, 5, 8, 9, 10], methodToCall))
print(findElement([1, 3, 5, 9], methodToCall))
print(findElement([1,3,2,4,6], methodToCall))