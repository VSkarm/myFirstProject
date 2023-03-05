def BasicRomanNumerals(strParam):
    charList = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    valList = [1,5,10,50,100,500,1000]
    value = 0
    last_val = 0

    for ch in strParam[::-1]:
        x = charList.index(ch)
        y = valList[x]

        if y >= last_val:
            value+=y
            last_val = y
        else:
            value -= y
    return value
print(BasicRomanNumerals(input()))