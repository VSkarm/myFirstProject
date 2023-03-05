def CountLetter(strArr):
    count = 0
    for string in strArr:
        count += string.count('a')
    return count

result = ['This is', 'a', 'very nice', 'array']
print(CountLetter(result))
