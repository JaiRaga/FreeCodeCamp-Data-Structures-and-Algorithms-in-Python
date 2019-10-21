def titleCase(sen):
    s = sen.lower().split(' ')
    w = []
    for i in s:
        l = [j for j in i]
        l[0] = l[0].upper()
        l = "".join(l)
        w.append(l)
    w = " ".join(w)
    return w


print(titleCase("I'm a little tea pot"))
print(titleCase("sHoRt AnD sToUt"))
print(titleCase("HERE IS MY HANDLE HERE IS MY SPOUT"))
print(titleCase('true'))
