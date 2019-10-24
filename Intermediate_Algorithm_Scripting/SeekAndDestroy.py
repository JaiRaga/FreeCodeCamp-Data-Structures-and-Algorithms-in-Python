def destroyer(*args):
    li = []
    newli = []
    for i in range(1,len(args)):
        li.append(args[i])
    for i in args[0]:
        if li.count(i) == 0:
            newli.append(i)

    return newli



print(destroyer([1, 2, 3, 1, 2, 3], 2, 3))
print(destroyer([1, 2, 3, 5, 1, 2, 3], 2, 3))
print(destroyer([2, 3, 2, 3], 2, 3))
print(destroyer(["tree", "hamburger", 53], "tree", 53))
print(destroyer(["possum", "trollo", 12, "safari", "hotdog", 92, 65, "grandma", "bugati", "trojan", "yacht"], "yacht", "possum", "trollo", "safari", "hotdog", "grandma", "bugati", "trojan"))