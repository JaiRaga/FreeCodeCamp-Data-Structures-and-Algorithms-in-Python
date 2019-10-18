def reverseString(s):
    newStr = ''
    for i in s:
        newStr = i + newStr
    return newStr



print(reverseString("hello"))
print(reverseString("Howdy"))
print(reverseString("Greetings from Earth"))
print(reverseString("12345"))