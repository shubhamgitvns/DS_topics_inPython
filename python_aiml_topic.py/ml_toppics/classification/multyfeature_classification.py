import pandas
import sys
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

X = df[features]
y = df['RESULT']

# initlize the decisiontree object
dtree = DecisionTreeClassifier()

# fit the data on tree
dtree = dtree.fit(X,y)


physics=[]
chemistry=[]
maths=[]
results=[]
marks={"PHY":[55],"CHEM":[39],"MTH":[55]}
examplemarks=pandas.DataFrame(marks)
print("Marks",examplemarks)
result=dtree.predict(examplemarks)
df=pandas.DataFrame({"RESULT":result})
df['TEXTRESULT'] = df['RESULT'].map(numbertoresult)
print(df['TEXTRESULT'][0])
physics.append(marks["PHY"][0])
chemistry.append(marks["CHEM"][0])
maths.append(marks["MTH"][0])
results.append(df["RESULT"][0])
print(maths)
