import pandas as pd


# Filter Data Frame
data = {
    'Title': ['Book1', 'Book2', 'Book3', 'Book4',"book5"],
    'Publication_Year': [1945, 1955, 1960, 2000, 2002],
    'Price':[10, 25, 15, 8,100]
}

# Creating the DataFrame
books_df = pd.DataFrame(data)
filter_price = books_df['Price']>=100 # this code check all the condition
print(filter_price)

filter_price2 = books_df[books_df['Price']>=100]
print(filter_price2)

filter_price3 = books_df.where(books_df['Price']>20)
print(filter_price3)