import pandas as pd

#single data print using df

#create
df=pd.DataFrame([1,2,3,4,5])
print("Simple Data Frame:",df)

# Sample data for demonstration
data = {
    'Title': ['Book1', 'Book2', 'Book3', 'Book4',"book5"],
    'Publication_Year': [1945, 1955, 1960, 2000, 2002],
    'Price':[10, 25, 15, 8,100]
}

# Creating the DataFrame
books_df = pd.DataFrame(data)
print(books_df)

# Filtering books published after 1950
recent_books = books_df[books_df['Publication_Year'] > 1950]
print("Books published after 1950:\n", recent_books)

# Filter books published after 1950 and priced less than $10
cheap_recent_books = books_df[(books_df['Publication_Year'] > 1950) & (books_df['Price'] < 10)]

print("Cheap books published after 1950:\n", cheap_recent_books)
print(type(df))


##2## Basic Data frame understanding
# head
books_head=books_df.head(2)
print(books_head)

#tail
books_tail=books_df.tail(2)
print(books_tail)

#shaape
books_shape = books_df.shape # the shape method finding the row and columnn in given data
print(books_shape)

#rename

books_column =  books_df.rename(columns={"Title": "Book_Title"},inplace=True)
print(books_column)
print(books_df)

# info
print("Information of book data")
books_df.info()
