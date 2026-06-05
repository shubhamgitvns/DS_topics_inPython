from sklearn.datasets import fetch_california_housing
import pandas as pd

housing = fetch_california_housing()

# print all about the data

# print(housing)
print("Keys:")
print(housing.keys())
print("Data:")
print(housing.data)
print("Target:")
print(housing.target)
print("Frame:")
print(housing.frame)
print("Target_name:")
print(housing.target_names)
print("Feature_name:")
print(housing.feature_names)
print("Descr:")
print(housing.DESCR)

