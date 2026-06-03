from sklearn import tree
import matplotlib.pyplot as plt

#Functions for pass and fail only
def divisions(n):
  # Convert numeric division code to text
  if n==2:
    return "fail"
  return "pass"
def classifications(n):
  # Less than 40 is fail and the numeric code is 2. 
# Pass numeric code is 1
  if n<40:
    return 2
  return 1

inputmarks=[50,45,66,7,89,21,39,40,89]
inputmarks.sort()
marks=[[x] for x in inputmarks]#Classification needs input as a 2d array
#Use one of the following three
results=[classifications(x) for x in inputmarks]#Calculated
textresults=[divisions(x) for x in results]# Print results in words

print(inputmarks, results, textresults)
