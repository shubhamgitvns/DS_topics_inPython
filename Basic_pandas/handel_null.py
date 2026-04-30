
import pandas as pd
import numpy as np
# Handle missing value
data = {
    'Title': ['Book1', 'Book2', 'Book3', 'Book4',"Book5"],
    'Publication_Year': [1945, 1955, 1960, 2000, 2002],
    'Price':[10, 25, 15, 8,100]
    
}

df = pd.DataFrame(data)

df.loc[df.Title == 'Book5', 'Price'] = np.nan
null_df = df.isnull() # This function check the nan value in boolian form 
print(null_df)
print(df[df.isnull().any(axis=1)]) # print only null row
print(df.isnull().sum()) # print the null column where the ull value exit

# fill the null value
# df = df.fillna(89)
# print(df)
# fill the data using inplace
df.fillna(0, inplace=True)
print(df)

