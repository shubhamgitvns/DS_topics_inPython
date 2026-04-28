import numpy as np
x=[1,2,3,4]
y=[4,6,8,10]
n= len(x)
cx=0
cy = 0
sigmaXY = 0
sigmaX2 = 0
print(n)
for i in range(len(x)):
    cx += x[i]
    cy += y[i]
    sigmaXY+= x[i]*y[i]
    sigmaX2 += x[i]*x[i]

b = (n * sigmaXY - cx * cy) / (n * sigmaX2 - cx * cx)
a= (cy-b*cx) / n
# print(f"a={a}")
# print(f"b={b}")
ppf= np.polyfit(x,y,1)
print(ppf)
