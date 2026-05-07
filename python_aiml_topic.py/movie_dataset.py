import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('hollywood_movies_sample.csv')

df["profit_million"] = df["revenue_million"] - df["budget_million"]

df["success"] = df["profit_million"].apply(
    lambda x: 1 if x > 0 else 0
)

# print(df[["title", "profit_million", "success"]])


genre_profit = df.groupby("genre")["profit_million"].mean()

# print(df['profit_million'])
# print(genre_profit)

# genre_profit.plot(kind="bar")
# plt.xlabel("Genre")
# plt.ylabel("Average Profit")
# plt.title("Average Profit by Genre")
# plt.show()


# 1 Q: Find top 5 highest revinue
# higest_revinue = df['revenue_million'].nlargest(5)
higest_revinue = df.nlargest(5,'revenue_million')[['title', 'revenue_million']]
print(higest_revinue)

# 2 Q: Find the average rating of all films
avg = df['rating'].mean()
print(avg)

# 3 Q: Find the total number of genres
print(df['genre'].count())

# 4 Q: Create a profit column
print(df)

# 5 Q: Find the most profitabel genre
print(df.nlargest(1,'profit_million')[['genre', 'profit_million']])

# 6 Q: Ploat budgte vs revinue
# plt.scatter(df['budget_million'], df['revenue_million'])
# plt.title('Budget vs Revinue')
# plt.xlabel('Budget')
# plt.ylabel('Revinue')
# plt.grid()
# plt.show()

#  7 Q:Build a hit/flop prediction model.
df["profit_per"] = df["profit_million"] / df["budget_million"]*100
df["result"] = df["profit_per"].apply(
    lambda x: 'flop' if x <= 0 else ('Hit' if x<=500 else 'Superhit')
)
print(df)