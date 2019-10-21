def frankenSplice(lis1, lis2, n):
    lis = lis2[:]
    for i in lis1:
        lis.insert(n, i)
        n += 1
    return lis

print(frankenSplice([1, 2, 3], [4, 5, 6], 1))
print(frankenSplice([1, 2], ["a", "b"], 1))
print(frankenSplice(["claw", "tentacle"], ["head", "shoulders", "knees", "toes"], 2))