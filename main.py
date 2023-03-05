boolean_true = True
boolean_false = False

a = 10
b = 20

c = a+ b
print(c)
c = b-a
print(c)
c = a*b
print(c)
c = b/a
print(c)
c = b//a
print(c)
c = b%a
print(c)

c = a == b
print("a is equal to b: ", c) # Output: a is equal to b: False
c = a!=b
print("a is not equal to b: ", c) # Output: a is not equal to b: True
c = a > b
print("a is greater than b: ", c) # Output: a is greater than b: False
c = a < b
print("a is less than b: ", c) # Output: a is less than b: True
c = a>=b
print("a is greater than or equal to b: ", c) # Output: a is greater than or equal to b: False
c = a<=b
print("a is less than or equal to b: ", c) # Output: a is less than or equal to b: True


a = "Geia sou"
b = "Xazepsame reeee"
c = a + " __+++__ "+b
print(c)

c = a[0]
print(c + " prwto psifio")
c = a[-1]
print(c + " teleytaio psifio")
c = a[0:5]
print("to substring "+c)

c = len(a)
print(c)

#slicing
a = "Hello World"
c = a[:5]
print (c+" travaei apo arxi mexri 5o psifio")
c = a[6:]
print(c+ " fernei to world")
c = a[-5:]
print(c + "tha vgalei to world")

a = " jOHANNES"
b = 30
c = "My name is {} and I am {} years old". format(a, b)
print("Formatting : ", c)

nums = [1,2,3,4,5]
f_num = nums[0]
print("first number is :", f_num)
last_num = nums[-1]
print("the last number in list is ", last_num)

fruits = ['aplle', 'banana', 'cherry']
fruits[0] = 'orange'
print("modified list of fruits ", fruits)


is_fruit = True
is_vegetable = False

if is_fruit:
    print("This is fruit")
else:
    print("This is not fruit")

if is_vegetable:
    print("This is veggie")
else:
    print("this is not veggie")
