def diffArray(lis1, lis2):
    lis = []
    for i in lis1:
        if lis2.count(i) == 0:
            lis.append(i)
    
    for i in lis2:
        if lis1.count(i) == 0:
            lis.append(i)
    
    return lis




print(diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]))
print(diffArray(["diorite", "andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"]))
print(diffArray(["andesite", "grass", "dirt", "dead shrub"], ["andesite", "grass", "dirt", "dead shrub"]))
print(diffArray([1, "calf", 3, "piglet"], [7, "filly"]))