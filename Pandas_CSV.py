#DEAL WITH CSV FORMAT
import pandas as pd
import numpy as np

df = pd.read_csv('finance_liquor_sales.csv')
print('Return the first 5 rows of the file imported\n',df.head())
print('Return the last 5 rows of the file imported\n',df.tail())
print('\nMore information about our dataset with info()\n')
print(df.info())
print('\nNumber of rows and Columns : df.shape\n')
print(df.shape)

#Analyzing Data with Pandas
print("\t mean()")
mean = df.mean(numeric_only=True)
print(mean)
print("\t median()")
median = df.median(numeric_only=True)
print(median)
print("\t max()")
max_v = df.max(numeric_only=True)
print(max_v)
print("\t summary")
summary = df.describe()
print(summary)

#GROUbY
print('\tGroup the data on category name value -groupby()')
cn = df.groupby('category_name')
print(cn.first())
print('\tGroup the data on category name value and on CITY where are sold!-groupby()')
cnc = df.groupby(['category_name', 'city'])
print(cnc.first())

print('\tGroup the data on category name value THEN compute the SUM of each group ')
df = pd.read_csv('finance_liquor_sales.csv')
cn = df.groupby('category_name')
# print(cn.aggregate(np.sum))
print("\t group data on category_name, and on city where sold. Diff aggregation on diff columns")
cn2 = df.groupby(['category_name', 'city'])
print(cn2.agg({'bottles_sold': 'sum', 'sale_dollars': 'mean'}))

#DATA FILTERING
print('group data on Vendor name value and filter data to return vendor_name which lived twenty or more times')
ng = df.groupby('vendor_name')
print(ng.filter(lambda x:len(x)>=20))


#CONCATENATION
print('\tCreate two dicts -->convert in DF -->use CONCAT to create one DF')
d1 = {
    'Name':['Mary', 'John', 'Alice', 'Bob'],
    'Age':[27, 24, 22, 32],
    'Position': ['Data Analyst', 'Trainee', "QA Tester", 'IT']
}
d2 = {
    'Name':['Steve', 'Tom', 'Jenny', 'Nick'],
    'Age':[37, 34, 32, 42],
    'Position': ['IT','Data Analyst', 'Consultant', "QA Tester", ]
}
df1 = pd.DataFrame(d1, index = [0,1,2,3])
df2 = pd.DataFrame(d2, index = ['a','b','c','d'])
result = pd.concat([df1, df2])
print(result)
print('create 2 dicts with names and age -->converted into DF--> merge into one with unique key combination')
d1 ={
    'key':['a','b','c','d'],
    'Name':['Mary', 'John', 'Alice', 'Bob']
}
d2 = {
    'key':['a','b','c','d'],
    'Age':[27,24,22,32]
}
df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)
result = pd.merge(df1, df2, on='key')
print(result)

print('\tdefine 2 dicts with employee data and convert to DF --> use join() to combine functions-->combine cols of these DFs into SINGLE DF getting !intersection!' )
d1 = {
    'Name':['Mary', 'John', 'Alice', 'Bob'],
    'Age':[27,24,42,32]
}
d2 = {
    'Pos':['DA','TRIN','QA', 'IT'],
    'Y_o_Exp':[5,10,15,20]
}
df1 = pd.DataFrame(d1, index=[0,1,2,3])
df2 = pd.DataFrame(d2, index=[0,2,3,4])
result = df1.join(df2, how = 'inner')
print(result)