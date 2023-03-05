# print("Mynameis") if input() == "Vasilis" else print("Nada")
L = ["me", "you", "he"]
for elem in range(len(L)):
    print(L[elem])
    print(L[elem])

list = ["a", "b", "c", "d", "e" ,"f"]
for i,m in enumerate(list):
    print(i," ",m)

for k in range (20, 40):
    if k == 30:
        print("kanw break")
        break
    if k % 2 == 0:
        print("Tsekarw to %")
        continue
    print(k)