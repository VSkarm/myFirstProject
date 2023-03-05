import matplotlib.pyplot as plt
import numpy as np

age = [10,20,30,40,50,60,70,80,90,100]
cardiac_cases = [5,15,20,40,55,55,70,80,90,95]
survival_chances = [99,99,90,90,80,75,60,50,30,25]
#
# plt.xlabel("Age")
# plt.ylabel("Precentage")
#
# plt.plot(age, cardiac_cases, color ='black', linewidth = 2, label = 'Cardiac Cases', marker ='o', markerfacecolor='red', markersize = 12)
# plt.plot(age, survival_chances, color ='yellow', linewidth=3, label= 'Survival Chances', marker = '^', markerfacecolor= 'green', markersize =12)
#
# plt.legend(loc = 'lower right', ncol =3)
# plt.show()

#eXAMPLE 2
products = np.array([['Mhla', 'Bananes'], ['Mosxari', 'Kotopoulo'], ['Glyko', 'Chikoulata'], ['Psari', 'Pswmi'], ['Avga', 'Mpeikon']])

random = np.random.randint(2, size =5) #randomized array. with 5 elems (0 or 1)
choices = []

counter = 0
for product in products:
    choices.append(product[random[counter]])
    counter+=1
print(choices)
precentages = []
for i in range(4):
    precentages.append(np.random.randint(25))
precentages.append(100-np.sum(precentages))
print(precentages)
plt.pie(precentages, labels = choices)
plt.legend(loc='lower right', ncol=1)

plt.show()
