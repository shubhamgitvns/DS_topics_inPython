import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
phy=[40,40,40,39]
chem=[40,39,40,40]
math=[40,40,39,40]
result = ["Pass","Fail","Fail","Fail"]
status = [1,0,0,0]
# ctreate the data frame tabel
df = pandas.DataFrame({'PHY':phy, 'CHEM': chem, 'MTH':math, 'RESULT': result, 'STATUS': status})
# print(df)

resulttonumber = {'Fail': 0, 'Pass': 1}
numbertoresult = {0: 'Fail', 1: 'Pass'}
# convert df in maping for resulttonumber
df['RESULT']= df['RESULT'].map(resulttonumber)
# print(df['RESULT'])
# convert df in maping for numbertoresult
df['STATUS']= df['STATUS'].map(numbertoresult)
# print(df['STATUS'])

features = ['PHY', 'CHEM', 'MTH']

x = df[features]
y = df['RESULT']

# initlize the decisiontree object
dtree = DecisionTreeClassifier()

# fit the data on tree
dtree = dtree.fit(x,y)
print(dtree)

