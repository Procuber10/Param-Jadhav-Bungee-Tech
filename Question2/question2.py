import pandas as pd

df = pd.read_csv (r'C:\Users\Param\OneDrive\Documents\main2.csv')
grp=df.groupby('occupation').agg({'age':['min','max']})
print(grp)
