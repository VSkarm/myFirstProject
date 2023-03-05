import matplotlib.pyplot as plt
import numpy as np
#plot() function
print('PLOT :draw a line from point to point\nTakes 2 params (x-axis, y-axis)')
# plt.plot([0,10], [0,300])
# plt.show()
print('plot ONLY points')
# plt.plot([0,10], [0,300], 'o')
# plt.show()
print('Print Multiple Points')
# plt.plot([0,2,4,6,8,10], [1,3,5,7,9,11])
# plt.show()
# plt.plot([0,2,4], [3,8,1], marker='^', ls ='dotted')

plt.title('Title')
plt.xlabel('X-aksonas')
plt.ylabel('Y-aksonas')
plt.grid()

# plt.subplot(2,1,1)
# plt.plot([0,2,4,6,8,10], [3,8,1,10,5,12])
# plt.subplot(2,1,2)
# plt.plot([0,10], [0,300])

# x = np.array([99,86,87,89,111,43,234,54,32,67])
# y = np.array([7,5,6,8,10,11,23,21,1,2])
# plt.scatter(x, y)
# plt.show()

#BAR CHART
z = np.array(['A', 'B', 'C', 'D'])
c = np.array([4,5,10,1])

plt.bar(z,c)
# plt.show()
#PIE CHART
mylabels = np.array(["potata", 'bacon', 'tomatoe', 'sausage'])
x = np.array([25,35,15,25])
plt.pie(x, labels = mylabels)
plt.legend() #add a list of explenation
plt.show()
