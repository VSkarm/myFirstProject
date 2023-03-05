import numpy as np
def p(string):
    print(string)
#1-d array  - uin-dimensional
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(arr)
print(type(arr))
#0-d Array --> SCALAR
arr1 = np.array(10)
print(arr1)

#2-D array --represent a matrix
arr2 = np.array([[1,2], [3,4]])
print(arr2)

#3D arrays:
arr3 = np.array([[[1,2],[3,4]], [[5,6],[7,8]]])
print(arr3)

#n-dim attribute
print(arr.ndim, arr1.ndim, arr2.ndim, arr3.ndim)


#INDEXING
print(arr[0], "1d")
print(arr2[1,1], " 2d")
print(arr2[1,-2], " negative index")

#ARRAY SLICING
print("####slicing")
print(arr[1:4])
print(arr[2:])
print(arr[:4])
print("Slicing with step~!arr[0:10:2]")
print(arr[0:10:2])
print("2_D SLICING arr2[1, 0:2]")
print(arr2[1, 0:2])

#COPY AND VIEW
copy = arr.copy()

copy[0] = 24
print(arr , ' array')
print(copy, 'copy !SAtarting array not affected !!\n')

view = arr.view()
view[0] =24

print(arr, '  arr~~~')
print(view, ' ~~ VIEW !! the starting array is also affected !!')

#SHAPE AND RESHAPE
print('\t SHAPE AND RESHAPE')
copy = arr2.copy()
print(arr2.shape, ' print arr.shape (2 dims__EACH DIM__ 2 elems')
print(" Doing a RESHAPE !")
arr_new =  np.array([1,2,3,4,5,6])
view = arr_new.view()
print(arr_new)
print(arr_new.reshape(2,3), "reshape (2,3)")

#SPLIT AND SEARCH
print("Split & Search")
arr_split = np.array([1,2,5,6,7,8,9,10])
arrList = np.array_split(arr_split,2)
for arr in arrList:
    print(arr)



print("Search __ σε ποιες θεσεις υπάρχει η τιμλή 2 στον παραπανω array")
print(arr_split)
print(np.where(arr_split == 2))
print('search even numbers of array\n')
print(np.where(arr_split % 2 ==0))

#SORTING ARRAYS
print("sort arrays")
arr = np.array([2,5,1,3,6,4])
print(arr)
print(np.sort(arr), 'Sort an array!')
arr = np.array([True, False, False, True])
print(np.sort(arr), ' soretd array of true and false')
arr = np.array(['Patates', "Mhla", 'Kima', 'Ntomates'])
print(arr)
print(np.sort(arr), 'sorted o apo panw pinakas\n')

#ARITHMETIC FUNCTIONS
print("\t Arithmetic Functions ~~ epistrefoun se new array")
arr1 = np.array([-1,2,-3,4])
arr2 = np.array([1,2,3,4])
print(np.add(arr1, arr2), f'kane add tous{arr1} kai {arr2} ')
print(np.subtract(arr1, arr2), f'kane SUBTRACT tous{arr1} kai {arr2} ')
print(np.multiply(arr1, arr2), f'kane MULTIPLY tous{arr1} kai {arr2} ')
print(np.divide(arr1, arr2), f'kane DIVIDE tous{arr1} kai {arr2} ')
print(np.power(arr1, arr2), f'kane raise to content tou {arr1} sto content tou  {arr2} ')
print(np.mod(arr1, arr2), f'kane MOD (%) tous{arr1} kai {arr2} ')
print(np.absolute(arr1), f'deikse to ABSOLUTE tou{arr1} ')

#ROUNDING DECIMALS
print('\trounding decimals')
arr = np.array([1.23, 3.45, 6.78])
print(np.trunc(arr), 'TRUNC()')
print(np.fix(arr), 'FIX()')
print('PIO PANW GINETAI REMOVE  TWN DECIMALS TOY ',arr)
print('USE THE around() to round off to specified amount of decimal points')
print(np.around(arr,1), 'np.around(arr,1) ston ', arr)
print('USE floor() and ceil() to round off decimal nearest lower and upper')
arr = np.array([1.23456, 2.9876])
print(np.floor(arr), 'floor', arr)
print(np.ceil(arr), 'ceil ', arr)

#NUMPY LOGS
print('\t Numpy LOGS')
arr = np.array([1,2,3,4])
print(np.log(arr), ' np.log(arr)', arr, ' base e log')
print(np.log2(arr), ' np.log2(arr)')
print(np.log10(arr), ' np.log10(arr)')

#NUMPY SUMMATIONS
print('\t numpy summations')
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
print(np.sum([arr1, arr2]), 'arr1, arr2')
print('summation by axis, numpy will sum the numbers in each array')
print(np.sum([arr1, arr2], axis = 1), ' np.sum([arr1, arr2], axis = 1)')
print(' Cummulative sum -- partially adding elements in array')
arr = np.array([1,2,3])
print(np.cumsum(arr), ' kanei cumsum(arr) dld edw [1, 1+2, 1+2+3] = ')

#numpy products
print('\t numpy products')
print(np.prod([arr1, arr2]), ' kanw prod twn arr1 kai arr2')
print(np.prod([arr1, arr2], axis = 1), 'kanw prod me axis 1, product for each array!!')
print(np.cumprod(arr1), ' cummulative product means partially multiplying elements of array ', arr1)

#LCM GCD
print('\tLowest Common Multiple Greatest Common Multiple')
arr = np.array([1,2,3,4,5])
print(np.lcm.reduce(arr), ' find lcm in arr ', arr, ' vazw kai reduce gia na ftiakse enan pin aka me ena stoixeio')
print(np.gcd.reduce(arr), ' find gcd in arr ', arr, ' vazw kai reduce gia na ftiakse enan pin aka me ena stoixeio\n')

#TRIGONOMETRIC FUNCTIONS
arr = np.array([np.pi/2, np.pi/3, np.pi/4])
print('use sin() cos() tan() that take radiant values and produce corresponding sin cos tan \n')
print(np.around(np.sin(arr), 8), ' sin')
print(np.around(np.cos(arr), 8), ' cos')

print('CONVERT RADIANS TO DEGREES AND VICE VERSA')
arr = np.array([90,180,360])
arr = np.deg2rad(arr)
print(arr, ' deg to rad')

arr = np.rad2deg(arr)
print(arr, ' rad to deg')
print(np.hypot(3, 4), ' print hypot(3,4) την υποτεινουσα')









