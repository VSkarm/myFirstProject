#return the number of duplicates in a list [1,2,2,2,3]
#returns 2 because 2 instances of '2'
def DistinctList(arr):
    arrset = set(arr)
    duplicates = len(arr) - len(arrset)

    return duplicates
print(DistinctList(input()))