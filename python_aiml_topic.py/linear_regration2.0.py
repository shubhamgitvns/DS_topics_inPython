
x=[8, 10, 12]
y=[10, 13, 16]
n = len(x)

mean_X= sum(x)/n
mean_Y= sum(y)/n
div_X = []
div_Y = []
p_of_d =[]
sqr_of_div_X = []


for i in range(n):
    
    div_X.append(x[i] - mean_X)

    div_Y.append(y[i] - mean_Y)

    p_of_d.append(div_X[i] * div_Y[i]) 
    sqr_of_div_X.append(div_X[i] * div_X[i])

sum_of_pd = sum(p_of_d)
sum_of_sqr_of_div_X = sum(sqr_of_div_X)



# linear regration = Y=mX+b
# slop/cooficent m = sum of product division / sum of sqt of division
# b = mean of y - (m* mean of x)

m = sum_of_pd / sum_of_sqr_of_div_X
b= mean_Y - (m * mean_X)

#prediction
X = 20
y = m * X + b
print("prediction", y)
    
