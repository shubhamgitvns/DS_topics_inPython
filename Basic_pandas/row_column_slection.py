import pandas as pd

#single data print using df


# Sample data for demonstration
data = {
    'Title': ['Book1', 'Book2', 'Book3', 'Book4',"book5"],
    'Publication_Year': [1945, 1955, 1960, 2000, 2002],
    'Price':[10, 25, 15, 8,100]
}

# Creating the DataFrame
books_df = pd.DataFrame(data)
# print(books_df)

# select the colun 
select_column =books_df[['Title','Price']]
# print(select_column)

# select the row
print("Differenece Between loc and iloc")
select_row = books_df.loc[0:2] # loc = labels of index
print(select_row)
print("-----------------\n")
select_index = books_df.iloc[0:2] # iloc- index of loc
print(select_index)

