import pandas as pd
import numpy as np

d1 = {
    'Name' : ['Pankaj', 'Meghna', 'David', 'Lisa'],
    'ID' : [1,2,3,4],
    'Salary' : [100,200,np.nan, pd.NaT],
    'Role' : ['CEO', None, pd.NaT, pd.NaT]
}

df = pd.DataFrame(d1)
print(df)
print()

print(df.head(2))
print()

print(df.tail(2))

print(df.isnull().sum())
print()
print(df.info())
print()

df1 = df.dropna()
print(df1)
print()

df1 = df.dropna(axis=1)
print(df1)
print()

df['Role'].fillna('CEO', inplace=True)
print(df)
