import pandas as pd
# Row and Columns opertaions (Add, Update, Delete)
data = {
    'Title': ['Book1', 'Book2', 'Book3', 'Book4',"book5"],
    'Publication_Year': [1945, 1955, 1960, 2000, 2002],
    'Price':[10, 25, 15, 8,100]
}

# Creating the DataFrame
books_df = pd.DataFrame(data)
# Add Columns
books_df['Auther'] = ['Rajnish Osho', 'Acharya Prsant', 'Shubham', 'Champak', 'Arvind']
books_df['Discount'] = books_df['Price'] - 5

# Add Row
books_df.loc[len(books_df)] = ['Book6', 1987, 89, 'ABC',85] 
 # update value
books_df.loc[0, 'Price']= 150
print(books_df)

# Delete the value
delete_book = books_df.drop(books_df[books_df.Price == 89].index) # remove row
delete_book = books_df.drop('Discount', axis =1) # remove column
print(delete_book)
