def factorialize(num):
    if num == 0:
        return 1
    return num * factorialize(num-1)


print(factorialize(5))
print(factorialize(10))
print(factorialize(20))
print(factorialize(0))