import matplotlib.pyplot as plt
def linear_prediction(x, y, X):

    n = len(x)

    mean_X = sum(x) / n
    mean_Y = sum(y) / n

    div_X = []
    div_Y = []

    sum_of_sqr_of_div_X = 0
    sum_of_pd = 0

    for i in range(n):

        div_X.append(x[i] - mean_X)

        div_Y.append(y[i] - mean_Y)

        sum_of_pd += div_X[i] * div_Y[i]

        sum_of_sqr_of_div_X += div_X[i] * div_X[i]

    # linear regression: Y = mX + b

    m = sum_of_pd / sum_of_sqr_of_div_X

    b = mean_Y - (m * mean_X)

    prediction = m * X + b

    return prediction


x = [8, 10, 12]
y = [10, 13, 16]

ans = linear_prediction(x, y, 20)

print("Prediction =", ans)

# Create the graph

# plt.scatter(x, y, color= "green")
# plt.scatter(X,prediction, color = "red")
# plt.xlabel("Pizza in (inches)")
# plt.ylabel("Price of Pizza")
# plt.title("Pizza price prdiction")
# plt.show()

    
