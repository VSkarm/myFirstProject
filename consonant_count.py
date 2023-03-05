#Brut Force
def ConsonantCount(strParam):
    number = 0
    consonant = 'qwrtpsdfgjklzxvbnm'

    for i in strParam.lower():
        if i in consonant:
            number+=1
    return number