#take str parameter and return the string
#true if equal number of x's and o's
def ExOh(str):
    x_count = str.count('x')
    o_count = str.count('o')
    # for char in str:
    #     if char == 'x':
    #         x_count+=1
    #     elif char=='o':
    #         o_count+=1
    return True if x_count == o_count else False

print(ExOh(input()))