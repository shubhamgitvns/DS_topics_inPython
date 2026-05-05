import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




df = pd.read_csv('hollywood_movies_sample.csv')
print(df)

df["profit_million"] = df["revenue_million"] - df["budget_million"]

genre_profit = df.groupby("genre")["profit_million"].mean()

print(df['profit_million'])
print(genre_profit)

genre_profit.plot(kind="pie")
plt.xlabel("Genre")
plt.ylabel("Average Profit")
plt.title("Average Profit by Genre")
plt.show()