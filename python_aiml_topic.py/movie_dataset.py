import pandas as pd
import numpy as np

df = pd.read_csv('hollywood_movies_sample.csv')
print(df)

df["profit_million"] = df["revenue_million"] - df["budget_million"]

df["success"] = df["profit_million"].apply(
    lambda x: 1 if x > 0 else 0
)

print(df[["title", "profit_million", "success"]])
