from sklearn import tree
import matplotlib.pyplot as plt

#Functions for pass and fail only
def divisions(n):
  # Convert numeric division code to text
  if n==0:
    return "fail"
  if n==3:
    return "Third Devision"
  if n ==2:
    return "Second Devision"
  return "First Devisison"

def classifications(n):
  # Less than 40 is fail and the numeric code is 0. 
# Pass numeric code is 1
  if n<40:
    return 0
  if n<50:
    return 3
  if n<60:
    return 2
  return 1

inputmarks=[50,45,66,7,89,21,39,40,89]
inputmarks.sort()
marks=[[x] for x in inputmarks]#Classification needs input as a 2d array

#Use one of the following three
results=[classifications(x) for x in inputmarks]#Calculated

textresults=[divisions(x) for x in results]# Print results in words

print(inputmarks, results, textresults)

# Create the desicion tree object or model
classifier = tree.DecisionTreeClassifier()

# train the model by using input data
model = classifier.fit(marks, results)

fullmarksrange=[x for x in range(101)]
fullresultrange=[model.predict([[x]])[0] for x in fullmarksrange]
# print(fullresultrange)

plt.plot(marks,results, color="red")
plt.scatter(marks,results, color="blue", marker='o')
plt.grid()
plt.title("Students marks")
plt.xlabel("Marks of Students")
plt.ylabel("Devision of Students")
plt.legend(["Actual Division","Actual Division"])
plt.show()
