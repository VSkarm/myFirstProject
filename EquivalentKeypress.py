def EquivalentKeyPress(strArr):
    words = []
    for i in strArr:
        s = ''
        i = i.replace(',','')
        i = i.replace("-B", "1")
        for n in i :
            if n =="1":
                s = s[:-1]
            else:
                s += n
            words.append(s)
    if words[0] == words[1]:
        return "TRUE"
    else:
        return "FALSE"
print(EquivalentKeyPress(input()))