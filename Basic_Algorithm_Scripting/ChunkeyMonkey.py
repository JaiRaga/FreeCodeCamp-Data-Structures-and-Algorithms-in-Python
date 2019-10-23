def chunkArrayInGroups(lis, size):
    div = len(lis) // size
    mod = len(lis) % size
    itr = div+mod
    li = []

    for i in range(0,len(lis),size):
        if i != itr:
            li.append(lis[i:i+size])
        else:
            li.append(lis[i:])
    return li


print(chunkArrayInGroups(["a", "b", "c", "d"], 2))
print(chunkArrayInGroups([0, 1, 2, 3, 4, 5], 3))
print(chunkArrayInGroups([0, 1, 2, 3, 4, 5], 4))
print(chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6], 3))
print(chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6, 7, 8], 2))