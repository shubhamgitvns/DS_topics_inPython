from sklearn.datasets import fetch_california_housing
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import pandas as pd

# loading the data from sckit lern datset
housing = fetch_california_housing()

# print all about the data
# print(housing)

# create the data frame for exploring data
df = pd.DataFrame(
    housing.data,
   columns= housing.feature_names
)
# create the price column on dataset
df['Price']= housing.target

# drop the unnecessory data
df = df.drop(1)

# read the feature and target data
X = df.drop(['Price', 'Latitude', 'Longitude'], axis=1)
y = df['Price']

# train and split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# create the model
model = DecisionTreeRegressor(random_state=42)

#train the model
model = model.fit(X,y)


print("\nEnter House Details\n")

# User Inputs
income = float(input("Median Income: "))
house_age = float(input("House Age: "))
avg_rooms = float(input("Average Rooms: "))
avg_bedrooms = float(input("Average Bedrooms: "))
population = float(input("Population: "))
avg_occupancy = float(input("Average Occupancy: "))

# Predict
new_house = [[
    income,
    house_age,
    avg_rooms,
    avg_bedrooms,
    population,
    avg_occupancy
]]

# predict the data
predicted_price = model.predict(new_house)

print("\nPredicted House Price:")
print(predicted_price[0])


# predictions = dtree.predict(X_test)

# print(predictions[:5])