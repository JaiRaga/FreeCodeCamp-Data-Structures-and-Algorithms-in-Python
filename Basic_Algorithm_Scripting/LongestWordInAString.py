def findLongestWordLength(s):
    s = s.split(" ")
    length = 0

    for i in s:
        if len(i) > length:
            length = len(i)
    return length



print(findLongestWordLength("The quick brown fox jumped over the lazy dog"))
print(findLongestWordLength("May the force be with you"))
print(findLongestWordLength("Google do a barrel roll"))
print(findLongestWordLength("What is the average airspeed velocity of an unladen swallow"))