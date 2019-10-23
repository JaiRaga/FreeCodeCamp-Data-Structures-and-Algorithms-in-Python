def mutation(lis):
    for i in range(len(lis)):
        lis[i] = lis[i].lower()
    for i in lis[1]:
        if lis[0].count(i) == 0:
            return False
    return True




print(mutation(["hello", "hey"]))
print(mutation(["hello", "Hello"]))
print(mutation(["zyxwvutsrqponmlkjihgfedcba", "qrstu"]))
print(mutation(["Mary", "Aarmy"]))
print(mutation(["Noel", "Ole"]))