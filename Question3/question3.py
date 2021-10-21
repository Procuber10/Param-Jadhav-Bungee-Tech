import pandas as pd

df = pd.read_csv(r'C:\Users\Param\OneDrive\Documents\main3.csv')

yellow = df.sort_values(['Yellow Cards'], ascending=[False])

red = yellow.sort_values(['Red Cards'], ascending=[False])

print(red[['Team', 'Yellow Cards', 'Red Cards']])