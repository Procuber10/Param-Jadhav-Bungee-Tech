import pandas as pd

df = pd.read_csv(r'C:\Users\Param\OneDrive\Documents\main.csv')
grp = df.groupby((df['Year'] // 10) * 10)
query = (
{"Population": "max", "Violent": "sum", "Property": "sum", "Murder": "sum", "Forcible_Rape": "sum", "Robbery": "sum",
 "Aggravated_assault": "sum", "Burglary": "sum", "Larceny_Theft": "sum", "Vehicle_Theft": "sum"})
updated_df = grp.aggregate(query)
print(updated_df)
