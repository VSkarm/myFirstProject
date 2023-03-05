def FizzBuzz(num):
    i = 1
    string = ''
    while(i <= int(num)):
        if (i%3 == 0) and (i%5==0):
            string += ' '+"FizzBuzz "
        elif (i%5==0):
            string += ' '+'Buzz '
        elif (i%3==0):
            string += ' '+'Fizz '
        else:
            string += ' '+str(i)
        i+=1
    return string

print(FizzBuzz(input()))