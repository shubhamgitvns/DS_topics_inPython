import pandas as pd
#Aggergration & Groping
data = {
    'Title': ['Book1', 'Book2', 'Book3', 'Book4',"book5"],
    'Publication_Year': [1945, 1955, 1960, 2000, 2002],
    'Price':[10, 25, 15, 8,100]
}
df = pd.DataFrame(data)
df['Month'] = ['Jan', 'Feb', 'Jan', 'Mar', 'Dec'] # Add the new Column

print(df)
print(df['Month'].value_counts) # print the all monts frequency

print(df[df['Month']=='Jan'].value_counts) # print specific month friquency


# group by
prise_sum= df.groupby('Month')['Price'].sum()
print(prise_sum) 
aggrigaation =df.groupby('Month').agg({'Price': 'mean', 'Title': 'count'})
print(aggrigaation)
