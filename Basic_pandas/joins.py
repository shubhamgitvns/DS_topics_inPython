import pandas as pd

df1 = pd.DataFrame({
    'Id': [1,2,3],
    'Name': ['A', 'B', 'C']
})
df2 = pd.DataFrame({
    'Id':[1,2,2,4],
    'Score': [88,96,77,79]
})

concat = pd.concat([df1,df2],axis=0) # add the two differnt data farme in on data frame
# axis=0 add as row top on top
# axis=1 add as column side on side
print(concat) 

# join or marge

# mrg = pd.merge(df1 ,df2,how='inner', on='Id') #mrge the tabel as inner join which choose comman ellement on both tabel throw the ID
mrg = pd.merge(df1 ,df2,how='right', on='Id')
print(mrg)
