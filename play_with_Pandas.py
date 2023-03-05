import pandas as pd
import numpy as np

#. create Pandas Series
print('\t ===Create Pandas Series===')
x = [23, 48, 19]
my_first_series = pd.Series(x)
print(my_first_series)

#2. create Pandas Dataframes
print('\t ===Create Data Structures ===')
data = {
    "students": ['emma', 'John', 'Boo'],
    "grades" : [12, 18, 17]
}
my_first_dataframe = pd.DataFrame(data)
print(my_first_dataframe)

#3. column selection
print('\t ===Column selection ===my_first_dataframe[students]')
print(my_first_dataframe['students'])

#4. Row  selection
print('\t ===Row Selection with loc[]===')
my_first_df = pd.DataFrame(data, index = ["a", "b", "c"])
first_row = my_first_df.loc['a']
print(first_row, ' print frist row  my_first_df.loc[\'a\']\n')

# 5. row selection with iloc
print("\t === row selection with iloc[] ===")
second_row = my_first_df.iloc[1]
print(second_row,'\n')

#6. Handle Missing Data
print("\t handling missing data\n")
print("Having defined my_first_df  with some missing values\n, "
      "we call the function \nisnull()\n to find out the missing values in DataFrame format.")
data = {
    "students" : ['Emma', 'John', np.nan, 'Bob'],
    "grades" : [12, np.nan, 18, 29]
    }
my_first_df = pd.DataFrame(data, index = ['alpha','beta','gamma','delts'])
print(my_first_df)
print(my_first_df.isnull())

print('replace Null WITH \'fillna\' from col students with' 'no name and NO GRADE to grade column')
my_first_df['students'].fillna('No Name', inplace = True)
my_first_df['grades'].fillna('No Grade', inplace=True)
print(my_first_df,"\n")
print('REPLACE STUDENT Bob with student Alice')
df2 = my_first_df.replace(to_replace='Bob', value='Alice')
print(df2, '\n')
print('We use the INTERPOLATE function to fill the missing values, using linear method.\nIt ignores index and treat values as equally spaced, filled with forward direction'
      "we call the function \nisnull()\n to find out the missing values in DataFrame format.")
data = {
    "students" : ['Emma', 'John', 'Malak', 'Bob'],
    "grades" : [12, np.nan, 18, np.nan]
    }
my_first_df= pd.DataFrame(data, index=['a','b','c','d'])
df = my_first_df.interpolate(method='linear', limit_direction='forward')
print(df)
print('\ndropna() function to remove the rows with missing values. use the inplace = True statement')
data = {
    "students" : ['Emma', 'John', 'Malak', 'Bob'],
    "grades" : [12, np.nan, 18, np.nan]
    }
my_first_df= pd.DataFrame(data, index=['a','b','c','d'])
my_first_df.dropna(inplace=True)
print(my_first_df, "\n opou vrei Nan moy to afairei entelws !!")

print('\n==Pandas Iterstions')
print('Iterstion in SERIES')
s = pd.Series(['workearly', 'e-learning', 'python'])
for index, value in s.items():
    print(f'Index :{index}, Value:{value}')

#Iteration in Dataframes
print('Iterate dataframes: iterrows()')
data = {
    "students" : ['Emma', 'John', 'Malak', 'Bob'],
    "grades" : [12, 13, 18, 19.5]
    }
my_first_df = pd.DataFrame(data, index=['a','b', 'c', 'd'])
for i,j in my_first_df.iterrows():
    print(i,j)
    print()
#Μετατρέπει το Dataframe σε List κσι εκτυπώνει κατάλληλα.
data = {
    'students':['Emma', 'John'],
    'grades':[12, 18.9]
    }
my_first_df = pd.DataFrame(data, index = ['a', 'b'])
columns = list(my_first_df)
for i in columns:
    print(my_first_df[i][1], ' \nkanei print to 2o stoixeio tou column thn 2h sthlh!')



