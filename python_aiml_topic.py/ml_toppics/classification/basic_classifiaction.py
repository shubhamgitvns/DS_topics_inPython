from sklearn import tree
import matplotlib.pyplot as plt

#Functions for pass and fail only
def result_in_text(n):
  # Convert numeric division code to text
  if n==0:

    return "Draw"
  
  if n ==2:

    return "Team 2 win"
  
  return "Team 1 win"

def classifications(n):
   
  # Less than 40 is fail and the numeric code is 0. 
# Pass numeric code is 1


 if n > 0:
    return 1
 elif n<0:
    return 2
 else:
    return 0

matchscore=[
   [180 - 180],
    [200-170],
    [150-160],
    [250-210],
    [175-175],
    [300-280],
    [110-130],
    [220-180]
    
  ]

matchs = matchscore 

results = [
    classifications(x[0]) for x in matchscore
]

final_result =[result_in_text(x) for x in results]

print("teams score= ",matchs),
print("teams result= ",results),
print("final result= ",final_result)


# Create the desicion tree object or model
classifier = tree.DecisionTreeClassifier()

# train the model by using input data

model = classifier.fit(matchs, results)

prediction = model.predict([[140-145]])

print("Prediction =", prediction[0])

print("Result =", result_in_text(prediction[0]))
