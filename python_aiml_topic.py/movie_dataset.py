import pandas as pd
import numpy as np

df = pd.read_csv('hollywood_movies_sample.csv')
df.loc[df.title == 'Sky Warriors', 'budget_million'] = np.nan


print(df)
# print(df.info())

# Basic statistics
# print(df.describe())

# Check missing values
# print(df.isnull().sum())

# List all genres
print('unoque data')
print(df["genre"].unique())

print('duplicates')
print(df["budget_million"].value_counts())