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
  # Less than 40 is fail and the numeric code is 2. 
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
