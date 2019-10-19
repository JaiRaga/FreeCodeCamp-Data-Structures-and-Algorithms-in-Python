def confirmEnding(s, target):
    return s[len(s)-len(target):] == target


print(confirmEnding("Bastian", "n"))
print(confirmEnding("Congratulation", "on"))
print(confirmEnding("Walking on water and developing software from a specification are easy if both are frozen", "specification"))
print(confirmEnding("If you want to save our world, you must hurry. We dont know how much longer we can withstand the nothing", "mountain"))
print(confirmEnding("Abstraction", "action"))
