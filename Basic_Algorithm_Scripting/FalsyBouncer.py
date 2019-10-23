def bouncer(lis):
    li = []
    for i in lis:
        if not(not i):
            li.append(i)
    return li


print(bouncer([7, "ate", "", False, 9]))
print(bouncer(["a", "b", "c"]))
print(bouncer([False, None, 0, None, ""]))
