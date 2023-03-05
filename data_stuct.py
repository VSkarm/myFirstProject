fruits =['apple', "banana", 'cherry', "date"]
#Indexing
print("First fruit:", fruits[0])
print("Second fruit ", fruits[1])
#Slicing
print("The first two fruits are ",fruits[:2])
print("The last two fruits", fruits[-2:])

nums = [1,3,4]
letters = ["a","b","c"]
#Concat
comb = nums+letters
print("concat", comb)
#Repete
rep = nums*3
print("repete ",rep)

#Methods LISTS
#Append
fruits.append("elderberry")
print(fruits, " INSERT to elderberry sto telos")
#Insert
fruits.insert(1,"ekana INSERT sth thssi 1")
print(fruits)

#Remove
fruits.remove("banana")
print(fruits, "Me remove")

#POP
poped = fruits.pop()
print("Ekana pop apo ti lista to ", poped, "/nKai pleon h lista einai:/n", fruits)

# SETS
fruits_new = ['apple', 'banana', 'cherry', 'date']
fruits_set = set(fruits_new)
print('To SET dhmiourghthke', fruits_set , "\n H Seira twn elems den thrhthke!!")

#sets UNION
fr1 = {'apple', 'banana', 'cherry'}
fr2 = {'date', 'fig', 'grape', "cherry", 'banana'}
fr_united = fr1.union(fr2)

print('H synenwsh twn sets dinei ...', fr_united)

#Intersection : contains all elems that ae common to both sets
fruits_intersection = fr1.intersection(fr2)
print('INTERSECTION twn fruits :', fruits_intersection)
