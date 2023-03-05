import pandas as pd

#task1 create and display a 1-dim array-like object
#containing the array L = [5,10,15,20,25]
L = [5,10,15,20,25]
ds = pd.Series(L)
print(ds)

#task2 Convert first COL of DF as a series
print('\timport PD -->define a dict-->convert dict to DF-->iloc to get first col')
d = {
    'col1':[1,2,3,4,5,6,7,8],
    'col2':[2,3,4,5,7,6,5,8],
    'col3':[9,8,7,3,4,5,6,7]
}
ds = pd.DataFrame(d)
s1 = ds.iloc[:, 0]
print('First Column !!')
print(s1)
print(type(s1))

#3
print('\t read csv data file and print first 20 rows')
df = pd.read_csv('data.csv')
print(df.head(20))

#4
print('\t Iterate through df Dataframe from previous task')
for i,j in df.iterrows():
    print(i,j)