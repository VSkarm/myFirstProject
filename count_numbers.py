import re

def CountNumbers(str):
    numbers = re.findall(r'\d+', str)
    return len(numbers)
result = CountNumbers("1awqsedrs@23Rf547")
print(result)

result = CountNumbers('1q2w3e4r5t6y7u8i9o')
print(result)