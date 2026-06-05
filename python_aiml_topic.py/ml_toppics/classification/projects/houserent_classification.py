from sklearn.datasets import fetch_california_housing
import pandas as pd

# loading the data from sckit lern datset
housing = fetch_california_housing()

# print all about the data
# print(housing)

# create the data frame for exploring data
df = pd.DataFrame(
    housing.data,
   columns= housing.feature_names
)
# create the price column on dataset
df['Price']= housing.target

# descrive the data or understand the datsets 
print(df.head())
print(df.info)
print(df.describe())
print(df.isnull().sum())

