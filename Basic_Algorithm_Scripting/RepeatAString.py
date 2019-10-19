def repeatStringNumTimes(s, num):
    newStr = ''
    if num <= 0:
        return ""
    for i in range(num):
        newStr += s
    return newStr



print(repeatStringNumTimes("*", 3))
print(repeatStringNumTimes("abc", 4))
print(repeatStringNumTimes("abc", -2))
print(repeatStringNumTimes("*", 8))
print(repeatStringNumTimes("qwerty", 3))