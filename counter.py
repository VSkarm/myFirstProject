from collections import Counter

mylist = ["a", "b", "c", "d", "e", "f"]
count = Counter(mylist)
print(Counter(mylist))

count.update(["a", "b"])
print("Updated", count)

print("Count \' b \': ", count["b"])

#Examples
def add_nims(a,b):
    return a+b
def conacat_strings(a,b):
    return a + b
def add_num_to_strin(num, string):
    return str(num) + string
def multi_string(string, times):
    return string*times
def convert_string_to_int(string):
    return int(string)
def is_palindrome(string):
    return string == string[::-1]
def count_char_occurance(string, char):
    return string.count(char)


c= add_nims(3,5)
print("Sum: ", c)
c = conacat_strings("Geia", "sou Mal")
print("Concatenated ", c)

result = add_num_to_strin(5,"mhla")

result = multi_string("Malaka", 100)
print("Result: ", result)

result = convert_string_to_int("123654")
print("Result: ", result)

result = is_palindrome("SerreS")
print("Palindrome result:", result)

result = count_char_occurance("Mississimiismimispi", "s")
print("Count occurnce of s in Mississimsis ", result)

my_list = [1,1,1,3,3,3,2,2,5,4,5,6,7,8,9,2,4,3,5,6,7,8,9,0,2,2,1,2,3,4]
counter = Counter(my_list)
print("Result: ", counter)
result = counter.most_common(3) #τα 3 πιο συχνά σε εμφανίσεις στοιχεία
print(result)
