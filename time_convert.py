def TimeConvert(num):
    num = int(num)
    hours = num // 60
    minuites = num % 60
    return f'{hours} : {minuites}'
print(TimeConvert(input()))