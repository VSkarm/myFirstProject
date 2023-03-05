import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('1.supermarket.csv')
q = data.groupby('item_name').quantity.sum()

plt.bar(q.index, q, color = ['orange', 'purple', 'yellow', 'red', 'green', 'blue', 'cyan'])
plt.xlabel('Items')
plt.xticks(rotation=10)
plt.ylabel('Number of Items Ordered')
plt.title('Most ordered S/M items')
plt.show()