import re
def CodelandUsernameValidationREGEX(str):
    pattern = "^[a-zA-z][a-zA-Z0-9_]{2,23}[a-zA-Z]$"
    match = re.match(pattern,str)
    if match:
        return "true"
    else:
        return "False"
def CodelandUsernameValidation(str):
    if len(str) >= 4 and len(str) <=25:
        if str[0].isalpha():
            if all(c.isalnum() or c =='_' for c in str[1:-1]):
                if str[-1] != "_":
                    return 'true'
    return "false"

str = "John_1"
str2 ='qwsaedrwdfkaj'
print(CodelandUsernameValidation(str))
print(CodelandUsernameValidationREGEX(str2))


